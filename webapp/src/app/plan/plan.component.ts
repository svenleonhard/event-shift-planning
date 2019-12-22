import { PlanningService } from './../planning.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-plan',
  templateUrl: './plan.component.html',
  styleUrls: ['./plan.component.css']
})
export class PlanComponent implements OnInit {

  plan: [any];

  constructor(public planningService: PlanningService) {
    this.planningService.getPlan().subscribe(plan => {
      console.log(plan);
      this.plan = plan;
    });
  }

  ngOnInit() {
  }

}
