/* eslint-disable class-methods-use-this */
export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
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

  evacuationWarningMessage() {
    throw new Error('Everyone should evacuate the building');
  }
}
