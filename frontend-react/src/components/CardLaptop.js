import React from 'react';
import styles from '../styles/CardLaptop.module.css';

function CardLaptop() {
  return (
    <div className={styles.container}>
      <div>
        <img src="/images/laptop.png" width="90%" height="90%" alt="laptop" />
      </div>
      <div className={styles.text__icon}>
        <h1>Apple Macbook Pro</h1>
        <p>stars</p>
        <p>
          $499 <span>$599</span>
        </p>
        <p>
          <button>Add to Cart</button>
        </p>
      </div>
    </div>
  );
}

export default CardLaptop;
