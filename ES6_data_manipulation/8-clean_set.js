export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
  // Convert Set to array
  return Array.from(set)
    // Filter values ​​that start with startString
    .filter((element) => typeof element === 'string' && element.startsWith(startString))
    // Extract the part after startString
    .map((element) => element.slice(startString.length))
    // Join values ​​with a separator
    .join('-');
}
