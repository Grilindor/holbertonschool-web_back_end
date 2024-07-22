export default function getStudentIdsSum(listStudents) {
  if (!Array.isArray(listStudents)) {
    return [];
  }
  // returns the sum of all the student id
  return listStudents.reduce((total, listStudent) => total + listStudent.id, 0);
}
