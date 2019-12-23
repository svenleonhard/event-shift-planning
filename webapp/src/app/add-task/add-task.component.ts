import { Component, OnInit, Input } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { PlanningService } from '../planning.service';

@Component({
  selector: 'app-add-task',
  templateUrl: './add-task.component.html',
  styleUrls: ['./add-task.component.css']
})
export class AddTaskComponent implements OnInit {

  taskForm;

  @Input()
  categories = [];

  constructor(
    private formBuilder: FormBuilder,
    private planningService: PlanningService
  ) {
    this.taskForm = this.formBuilder.group({
      description: '',
      category: this.categories
    });
  }

  ngOnInit() {
  }

  onSubmit(taskData) {
    console.log(taskData)

    this.taskForm.reset();
  }

}
