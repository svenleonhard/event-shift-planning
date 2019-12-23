import { PlanningService } from './../planning.service';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-plan',
  templateUrl: './plan.component.html',
  styleUrls: ['./plan.component.css']
})
export class PlanComponent implements OnInit {

  @Input()
  plan;

  constructor(public planningService: PlanningService) {
  }

  ngOnInit() {
  }

}
