import React from 'react';
import styles from '../styles/TopAdvertComponent.module.css';

function TopAdvertBox({ image, header, text }) {
  return (
    <div className={styles.container}>
      <div className={styles.image}>
        <img width="50" height="50" alt="" src={image} />
      </div>
      <h1>{header}</h1>
      <p>{text}</p>
    </div>
  );
}

export default TopAdvertBox;
