import React from 'react';
import styles from '../styles/MiddleAdvertBox.module.css';

function MiddleAdvertBox() {
  return (
    <div className={styles.container}>
      <h1 className={styles.header}>Latest News</h1>
      <div className={styles.box__container}>
        <div className={styles.outer__box}>
          <div className={styles.inner}>
            <img
              width="150px"
              height="120px"
              alt="iphone"
              src="/images/iphonefront.jpg"
            />
          </div>
          <div>
            <p>01 Jan 2022</p>
            <h1>Typesetting Industry</h1>
            <p>
              At vero eos et accusamus et iusto odio dignissimos ducimus qui
              blanditiis praesentium
            </p>
          </div>
        </div>
        <div className={styles.outer__box}>
          <div className={styles.inner}>
            <img
              width="150px"
              height="120px"
              alt="iphone"
              src="/images/iphonefront.jpg"
            />
          </div>
          <div>
            <p>01 Jan 2022</p>
            <h1>Typesetting Industry</h1>
            <p>
              At vero eos et accusamus et iusto odio dignissimos ducimus qui
              blanditiis praesentium
            </p>
          </div>
        </div>
        <div className={styles.outer__box}>
          <div className={styles.inner}>
            <img
              width="120px"
              height="120px"
              alt="iphone"
              src="/images/iphonefront.jpg"
            />
          </div>
          <div>
            <p>01 Jan 2022</p>
            <h1>Typesetting Industry</h1>
            <p>
              At vero eos et accusamus et iusto odio dignissimos ducimus qui
              blanditiis praesentium voluptatum
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MiddleAdvertBox;
