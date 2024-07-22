export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  if (!Array.isArray(listStudents)) {
    return [];
  }

  return listStudents
    .filter((listStudent) => listStudent.location === city)
    .map((listStudent) => {
      const objgrade = newGrades.find((grade) => grade.studentId === listStudent.id);
      return {
        ...listStudent,
        grade: objgrade ? objgrade.grade : 'N/A',
        // return "N/A" if no note find
      };
    });
}
