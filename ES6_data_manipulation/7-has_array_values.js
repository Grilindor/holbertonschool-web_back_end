export default function hasValuesFromArray(set, array) {
  // By combining every and has, we can check that each element of the array exists in the Set.
  return array.every((element) => set.has(element));
}
