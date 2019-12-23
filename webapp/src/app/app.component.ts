import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'webapp';

  categories = [];
  employees = [];

  categoryAdded(categories) {
    this.categories = categories;
  }

  employeeAdded(employeeItem) {
    this.employees.push(employeeItem);
  }

}
