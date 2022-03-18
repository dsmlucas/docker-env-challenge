export const DATE_PATTERNS = {
  PT_BR: 'dd/MM/yyyy',
  PT_BR_HOUR: 'dd/MM/yyyy HH:mm',
  ISO: "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'",
  EN_US: 'yyyy-MM-dd',
  HOUR: 'HH:mm',
};

const format = (
  unformatted: string | Date,
  pattern = DATE_PATTERNS.PT_BR_HOUR,
): string => {
  let dt;

  if (!unformatted) return '-';
  else if (typeof unformatted === 'string') dt = new Date(unformatted);
  else dt = unformatted;

  const year = dt.getFullYear();
  const month = String(dt.getMonth() + 1).padStart(2, '0');
  const day = String(dt.getDate()).padStart(2, '0');
  const hour = String(dt.getHours()).padStart(2, '0');
  const min = String(dt.getMinutes()).padStart(2, '0');

  switch (pattern) {
    case DATE_PATTERNS.PT_BR:
      return `${day}/${month}/${year}`;

    case DATE_PATTERNS.PT_BR_HOUR:
      return `${day}/${month}/${year} ${hour}:${min}`;

    case DATE_PATTERNS.EN_US:
      return `${year}-${month}-${day}`;

    case DATE_PATTERNS.HOUR:
      return `${hour}:${min}`;

    default:
      return 'Pattern not found!';
  }
};

export default {
  format,
};
