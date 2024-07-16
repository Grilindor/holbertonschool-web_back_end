function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const currentYear = getCurrentYear();
  return {
    [`income-${currentYear}`]: income,
    [`gdp-${currentYear}`]: gdp,
    [`capita-${currentYear}`]: capita,
  };
}

/*créer une variable const qui reprend les variable*/
/*En stockant le résultat de getCurrentYear() dans une variable currentYear,
nous évitons d'appeler la fonction plusieurs fois,
 ce qui rend le code plus efficace.*/
