import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CotizacionService {
  private apiUrl = 'http://localhost:8000/cotizaciones';

  constructor(private http: HttpClient) {}

  generarCotizacion(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }

  obtenerCotizaciones(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
