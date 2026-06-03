import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import glossary from '@site/src/data/glossary';
import styles from './styles.module.css';

const MAX_CHARS = 160;

export default function Term({ id, children }) {
  const [visible, setVisible] = useState(false);
  const entry = glossary[id];

  if (!entry) return <>{children}</>;

  const isLong = entry.definition.length > MAX_CHARS;
  const displayDef = isLong
    ? entry.definition.slice(0, MAX_CHARS).trim() + '...'
    : entry.definition;

  return (
    <span
      className={styles.term}
      onMouseEnter={() => setVisible(true)}
      onMouseLeave={() => setVisible(false)}
      onFocus={() => setVisible(true)}
      onBlur={() => setVisible(false)}
    >
      {children}
      {visible && (
        <span className={styles.tooltip} role="tooltip">
          <strong className={styles.tooltipTitle}>{entry.term}</strong>
          <span className={styles.tooltipDef}>{displayDef}</span>
          {isLong && (
            <Link to={`/glosario#${id}`} className={styles.glossaryLink}>
              Ver definición completa →
            </Link>
          )}
        </span>
      )}
    </span>
  );
}
