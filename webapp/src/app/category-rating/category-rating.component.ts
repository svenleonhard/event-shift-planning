import { Component, OnInit, Output, EventEmitter, Input, HostListener } from '@angular/core';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-category-rating',
  templateUrl: './category-rating.component.html',
  styleUrls: ['./category-rating.component.css']
})
export class CategoryRatingComponent implements OnInit {

  ratingLevel = 1;

  @Input()
  category;

  @Input()
  parentSubject: Subject<any>;

  @Output()
  ratingChanged = new EventEmitter<any>();

  constructor() { }

  ngOnInit() {
    this._buildRatingLevel();

    this.parentSubject.subscribe(event => {
      this.ratingLevel = 1;
    });

  }

  onChange() {
    this._buildRatingLevel();
  }

  _buildRatingLevel() {
    const  rating = {
      category : this.category,
      ratingLevel : this.ratingLevel
    };

    this.ratingChanged.emit(rating);
  }

}
