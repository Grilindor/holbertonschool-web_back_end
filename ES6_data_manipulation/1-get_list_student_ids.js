export default function getListStudentIds(listStudents) {
  // controle if it's a array
  if (!Array.isArray(listStudents)) {
    return [];
  }
  // return the extracted id in array
  return listStudents.map((listStudent) => listStudent.id);
}
