import React from 'react';
import styles from '../styles/AdvertComponent.module.css';
import TopAdvertBox from './TopAdvertBox';
import MiddleAdvertBox from './MiddleAdvertBox';

function AdvertComponent() {
  return (
    <div className={styles.container}>
      <div className={styles.first__row}>
        <div>
          <TopAdvertBox
            image="/images/freeshipping.png"
            header="free shipping"
            text="Sed ut perspiciatis unde omnis iste natus error 
            sit voluptatemaccusantium doloremque laudantium, totam rem aperiam, 
            eaque ipsa quae ab illo inventore veritatis et quasi architecto 
            beatae vitae dicta suntexplicabo"
          />
        </div>
        <div>
          <TopAdvertBox
            image="/images/refund.png"
            header="100% refund"
            text="dolore magnam aliquam quaerat voluptatem. 
            Ut enim ad minima veniam, quis nostrum exercitationem 
            ullam corporis suscipit laboriosam, nisi ut aliquid 
            ex ea commodi consequatur? Quis autem vel eum iure"
          />
        </div>
        <div>
          <TopAdvertBox
            image="/images/support.png"
            header="support 24/7"
            text="aspernatur aut odit aut fugit, sed quia 
            consequuntur magni dolores eos qui ratione 
            voluptatem sequi nesciunt. Neque porro quisquam 
            "
          />
        </div>
      </div>
      <div className={styles.second__row}>
        <MiddleAdvertBox />
      </div>
      <div className={styles.third__row}>third</div>
    </div>
  );
}

export default AdvertComponent;
