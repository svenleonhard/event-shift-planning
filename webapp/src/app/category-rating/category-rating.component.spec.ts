import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoryRatingComponent } from './category-rating.component';

describe('CategoryRatingComponent', () => {
  let component: CategoryRatingComponent;
  let fixture: ComponentFixture<CategoryRatingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CategoryRatingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CategoryRatingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
