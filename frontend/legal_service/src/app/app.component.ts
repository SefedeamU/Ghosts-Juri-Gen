import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CotizacionService } from './services/cotizacionService';
import { IaService } from './services/iaService';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, RouterModule, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'legal_service';

  form = {
    nombre: '',
    correo: '',
    tipoServicio: '',
    descripcion: ''
  };

  cotizacion: any = null;
  iaRespuesta: any = null;
  loading = false;
  error = '';

  cotizaciones: any[] = [];
  loadingCotizaciones = false;

  analisisIA: any = null;

  constructor(
    private cotizacionService: CotizacionService,
    private iaService: IaService
  ) {}

  ngOnInit() {
    this.cargarCotizaciones();
  }

  async generarCotizacion() {
    this.loading = true;
    this.error = '';
    this.cotizacion = null;
    this.iaRespuesta = null;

    // Validar tipo de servicio antes de enviar
    const tiposValidos = [
      "Constitución de empresa",
      "Defensa laboral",
      "Consultoría tributaria"
    ];
    if (!tiposValidos.includes(this.form.tipoServicio)) {
      this.error = 'Tipo de servicio no válido';
      this.loading = false;
      return;
    }

    try {
      const payload = {
        nombre_cliente: this.form.nombre,
        email: this.form.correo,
        tipo_servicio: this.form.tipoServicio,
        descripcion: this.form.descripcion
      };
      console.log('Enviando a backend:', payload);
      const cotResp = await this.cotizacionService.generarCotizacion(payload).toPromise();
      this.cotizacion = cotResp;
      this.cargarCotizaciones();
    } catch (err: any) {
      this.error = 'Error al generar la cotización';
      console.error(err);
    }
    this.loading = false;
    this.form = {
      nombre: '',
      correo: '',
      tipoServicio: '',
      descripcion: ''
    };
  }

  cargarCotizaciones() {
    this.loadingCotizaciones = true;
    this.cotizacionService.obtenerCotizaciones().subscribe({
      next: (data) => {
        this.cotizaciones = data;
        this.loadingCotizaciones = false;
      },
      error: () => {
        this.loadingCotizaciones = false;
      }
    });
  }

  analisisIAMap: {[numeroCotizacion: string]: any} = {};

  analizarCotizacion(cotizacion: any) {
    this.analisisIAMap[cotizacion.numero_cotizacion] = { cargando: true };
    this.iaService.analizarCotizacion(cotizacion).subscribe({
      next: (resp) => {
        this.analisisIAMap[cotizacion.numero_cotizacion] = resp;
      },
      error: () => {
        this.analisisIAMap[cotizacion.numero_cotizacion] = { propuesta_texto: 'Error al analizar la cotización.' };
      }
    });
  }
}
