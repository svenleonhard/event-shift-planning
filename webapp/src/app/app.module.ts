import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './navbar/navbar.component';
import { PlanComponent } from './plan/plan.component';
import { AddEmployeeComponent } from './add-employee/add-employee.component';
import { AddCategoryComponent } from './add-category/add-category.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { AddTaskComponent } from './add-task/add-task.component';
import { CategoryRatingComponent } from './category-rating/category-rating.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    PlanComponent,
    AddEmployeeComponent,
    AddCategoryComponent,
    AddTaskComponent,
    CategoryRatingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
