export default function updateUniqueItems(map) {
  // Check if the argument is an instance of Map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  // Using Array.from to convert iterator to array and then modify Map
  Array.from(map.entries()).forEach(([key, value]) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });
}
