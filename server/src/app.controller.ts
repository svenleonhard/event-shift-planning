import { Controller, Get, Post, Logger, Body } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post()
  makePlan(@Body()planConfig: any): any {
    return this.appService.getPlan(planConfig).then(plan => {
      return plan;
    });
  }
}
