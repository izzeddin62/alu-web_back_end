export default function cleanSet(set, substring) {
  if (!set || !substring) return '';
  return [...set].filter((el) => el.startsWith(substring)).map((el) => el.replace(substring, '')).join('-');
}
