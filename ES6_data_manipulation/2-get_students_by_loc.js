export default function getStudentsByLocation(listStudents, city) {
  if (!Array.isArray(listStudents)) {
    return [];
  }
  return listStudents.filter((listStudent) => listStudent.location === city);
  // returns an array of objects who are located in a specific city.
}
