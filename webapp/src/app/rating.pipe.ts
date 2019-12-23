import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'rating'
})
export class RatingPipe implements PipeTransform {

  rating = ['No', 'No matter', 'Yes']

  transform(value: number): any {
    return this.rating[value];
  }

}
