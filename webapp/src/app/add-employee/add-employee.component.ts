import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { PlanningService } from '../planning.service';
import { CategoryRatingComponent } from '../category-rating/category-rating.component';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-add-employee',
  templateUrl: './add-employee.component.html',
  styleUrls: ['./add-employee.component.css'],
})
export class AddEmployeeComponent implements OnInit {

  employeeForm;
  rating = {};


  @Input()
  categories = [];

  @Input()
  parentSubject: Subject<any> = new Subject();

  constructor(
    private formBuilder: FormBuilder,
    private planningService: PlanningService
  ) {
    this.employeeForm = this.formBuilder.group({
      name: ''
    });
  }

  ngOnInit() {
  }

  onRatingChanged(rating) {

    this.rating[rating.category.description] = rating.ratingLevel;
    console.log(this.rating)
    console.log(rating)
  }

  onSubmit(employee) {

    console.log({
      employee,
      rating: this.rating
    })
    this.employeeForm.reset();
    this.parentSubject.next('some value');
  }

}
