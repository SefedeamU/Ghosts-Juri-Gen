import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class IaService {
  private apiUrl = 'http://54.161.6.11:8001/analizar';

  constructor(private http: HttpClient) {}

  analizarCotizacion(cotizacion: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, cotizacion);
  }
}
