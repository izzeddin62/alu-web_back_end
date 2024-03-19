export default function divideFunction(numerator, denominator) {
  try {
    return numerator / denominator;
  } catch (error) {
    throw new Error('cannot divide by zero');
  }
}
