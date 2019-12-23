import { PlanningService } from './../planning.service';
import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-add-category',
  templateUrl: './add-category.component.html',
  styleUrls: ['./add-category.component.css']
})
export class AddCategoryComponent implements OnInit {

  @Output()
  categoryAdded = new EventEmitter<any>();

  categoryForm;

  constructor(
    private formBuilder: FormBuilder,
    private planningService: PlanningService
  ) {
    this.categoryForm = this.formBuilder.group({
      description: ''
    });
  }

  ngOnInit() {}

  onSubmit(category) {
    this.planningService.addCategory(category);

    this.categoryAdded.emit(this.planningService.getCategories());

    this.categoryForm.reset();
  }
}
