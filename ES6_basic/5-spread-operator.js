export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}

/*
...array1 et ...array2 et ...string décomposent les éléments de array1 et
array2 et string respectivement dans le tableau
*/
