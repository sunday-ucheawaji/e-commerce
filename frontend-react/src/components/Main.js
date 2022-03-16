import React from 'react';
import styles from '../styles/Main.module.css';
import CardLaptop from './CardLaptop';

function Main() {
  return (
    <div className={styles.container}>
      <div className={styles.slider}>
        <div className={styles.arrow__left}>
          <img
            src="/images/icons/arrow-down.svg"
            alt="down arrow"
            width={15}
            height={15}
            className={styles.svg}
          />
        </div>
        <div className={styles.text}>
          <h1>iPhone X</h1>
          <p>
            Relations to gain normal forms. Unfortunately, the names are the
            same, but the meaning is overloaded. Again,we appeal to intuition to
            understand this rule.
          </p>
          <h3>More</h3>
        </div>
        <div className={styles.phone}>
          <img
            src="/images/mask.png"
            height="100%"
            width="65%"
            alt="iphone ad"
          />
        </div>
        <div className={styles.arrow__right}>
          <img
            src="/images/icons/arrow-down.svg"
            alt="down arrow"
            width={15}
            height={15}
            className={styles.svg}
          />
        </div>
      </div>
      <div className={styles.below__slider}>
        <div>
          <img
            src="/images/iphone_ad.png"
            height={280}
            width={380}
            alt="iphone ad"
          />
        </div>
        <div>
          <img
            src="/images/occulus.png"
            height={280}
            width={380}
            alt="iphone ad"
          />
        </div>
        <div>
          <img
            src="/images/go_pro_ad_fumlul.png"
            height={280}
            width={380}
            alt="iphone ad"
          />
        </div>
      </div>
      <div className={styles.middle}>
        <div className={styles.best__seller}>BEST SELLER</div>
        <nav className={styles.nav}>
          <ul>
            <li>
              <a href="#">All</a>
            </li>

            <li>
              <a href="#">IPhone</a>
            </li>
            <li>
              <a href="#">IPad</a>
            </li>
            <li>
              <a href="#">Macbook</a>
            </li>
            <li>
              <a href="#">Accessories</a>
            </li>
          </ul>
        </nav>
        <div className={styles.products__grid}>
          <CardLaptop />
          <CardLaptop />
          <CardLaptop />
          <CardLaptop />
          <CardLaptop />
          <CardLaptop />
        </div>
        <h4 className={styles.load__more}>
          <a>Load More</a>
        </h4>
      </div>
      <div className={styles.lower__container}>
        <div className={styles.iphone__text}>
          <h1>iPhone 6 Plus</h1>
          <p>Performance and design. Taken right to the edge.</p>
          <p>
            <a>SHOP NOW</a>
          </p>
        </div>
        <div className={styles.iphone__img}>
          <img src="/images/iphone6.png" width="677px" height="709px" alt="" />
        </div>
      </div>
    </div>
  );
}

export default Main;
