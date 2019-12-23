import { Controller, Get, Post, Logger, Body } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post()
  makePlan(@Body() planConfig: any): any {
    Logger.log('Make Plan');
    return this.appService.getPlan(planConfig).then(plan => {
      Logger.log('plan finished:');
      Logger.log(plan);
      return plan;
    });
  }
}
