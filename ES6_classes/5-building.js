/* eslint-disable class-methods-use-this */
export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (!this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw TypeError('sqft must be a number');
    }
    this._sqft = newSqft;
  }
}
