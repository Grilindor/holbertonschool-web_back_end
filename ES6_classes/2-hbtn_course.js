class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

    set name(nname) {
      if (typeof nname !== 'string') {
          throw new TypeError('Name must be a string');
      }
      this._name = nname;
  }

  get length() {
      return this._length;
  }

  set length(nlength) {
      if (typeof nlength !== 'number') {
          throw new TypeError('Length must be a number');
      }
      this._length = nlength;
  }

  get students() {
      return this._students;
  }

  set students(nstudent) {
      if (!Array.isArray(nstudent) || nstudent.some((student) => typeof student !== 'string')) {
          throw new TypeError('Students must be an array of strings');
      }
      this._students = nstudent;
  }
}

export default HolbertonCourse;
