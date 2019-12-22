import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlanningService {

  url = 'http://localhost:3000/';

  constructor(public http: HttpClient) { }

  getPlan(): Observable<any> {
    return this.http.get<any>(this.url + 'plan');
  }
}
