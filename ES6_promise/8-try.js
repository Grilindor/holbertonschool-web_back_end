export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    // throw a new error with a personal message
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
