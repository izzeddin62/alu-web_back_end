export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  for (const item of array) {
    result.push(item + appendString);
  }

  return result;
}
