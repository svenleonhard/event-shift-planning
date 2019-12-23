import { Component, EventEmitter, Output } from '@angular/core';
import { PlanningService } from './planning.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'webapp';

  constructor(
    private planningService: PlanningService
  ) {

  }

  categories = [];
  employees = [];
  plan = [];

  categoryAdded(categories) {
    this.categories = categories;
  }

  employeeAdded(employeeItem) {
    this.employees.push(employeeItem);
  }

  makePlan() {

    console.log('make planpressed');
    const planConfig = {
      categories: this.categories,
      employees: this.employees
    };

    this.planningService.makePlan(planConfig).subscribe(plan => {
      this.plan = plan;
    });
  }

}
