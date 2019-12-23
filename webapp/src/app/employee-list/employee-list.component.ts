import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.css']
})
export class EmployeeListComponent implements OnInit {

  public isCollapsed = false;

  @Input()
  employeeItem;

  constructor() { }

  ngOnInit() {
  }

}
