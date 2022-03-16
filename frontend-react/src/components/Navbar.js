import React from 'react';
import styles from '../styles/Navbar.module.css';
// import Button from '@mui/material/Button';
// import AccessAlarmIcon from '@mui/icons-material/AccessAlarm';

function Navbar() {
  return (
    <div className={styles.container}>
      <div className={styles.top__nav}>
        <div className={styles.common}>
          <div className={styles.select}>
            <div>EN</div>
            <div>
              <img
                src="/images/icons/arrow-down.svg"
                alt="down arrow"
                width={15}
                height={15}
                className={styles.svg}
              />
            </div>
          </div>
          <div className={styles.select}>
            <div>USD</div>
            <div>
              <img
                src="/images/icons/arrow-down.svg"
                alt="down arrow"
                width={15}
                height={15}
                className={styles.svg}
              />
            </div>
          </div>
        </div>
        <div className={styles.common}>
          <div className={styles.select}>
            <div>
              <img
                src="/images/icons/profile-image.png"
                alt="down arrow"
                width={25}
                height={25}
                className={styles.svg}
              />
            </div>
            <div>My profile</div>
          </div>
          <div className={styles.select}>
            <div>
              <img
                src="/images/icons/cart.png"
                alt="cart"
                width={25}
                height={25}
                className={styles.svg}
              />
            </div>
            <div>0</div>
            <div>$500</div>
          </div>
          <div>
            <img
              src="/images/icons/search.svg"
              alt="search"
              width={25}
              height={25}
              className={styles.svg}
            />
          </div>
          <div>Register</div>
          <div>Login</div>
        </div>
      </div>
      <div className={styles.bottom__nav}>
        <div className={styles.logo}>BOUNCER</div>
        <nav className={styles.nav}>
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">Store</a>
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
      </div>
    </div>
  );
}

export default Navbar;
