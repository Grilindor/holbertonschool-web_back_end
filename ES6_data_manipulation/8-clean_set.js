export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
  // Convert Set to array
  return Array.from(set)
    .filter((element) => typeof element === 'string' && element.startsWith(startString))
    // Extract the part after startString
    .map((element) => element.slice(startString.length))
    .join('-');
}
