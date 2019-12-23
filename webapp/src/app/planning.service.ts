import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlanningService {

  url = 'http://localhost:3000';
  categeories = [];

  constructor(public http: HttpClient) { }

  makePlan(planConfig: any): Observable<any> {
    console.log('pc');
    console.log(planConfig);

    return this.http.post<any>(this.url, planConfig);
  }

  addCategory(categroy) {
    this.categeories.push(categroy);
  }

  getCategories() {
    return this.categeories;
  }
}
