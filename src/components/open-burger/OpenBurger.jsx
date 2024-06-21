import Header from '../header/Header';
import Buttons from '../ui/buttons/Buttons';
import Layout from '../layout/Layout';

import { arrayButtonsBurgerMenu } from './buttonsBurger.data';

import styles from './OpenBurger.module.scss';

const OpenBurger = () => {
  return (
    <Layout >
      <Header />
      <div className={styles.buttons__wrapper__openBurger}>
        {arrayButtonsBurgerMenu.map(button => (
          <Buttons
            key={button.id}
            id={button.id}
            path={button.path}
            leftIcon={button.leftIcon}
            rightIcon={button.rightIcon}
            title={button.title}
          />
        ))}
      </div>
      <div className={styles.openBurger__info}>
        <span className={styles.openBurger__text}>Оформить заказ по телефону</span>
        <a href="tel:+88002004445" className={styles.openBurger__phone}>8 800 200-44-45</a>
        <div className={styles.openBurger__socials}>
          <div className={styles.openBurger__social}><img src="/icons/open-burger-menu/youtube.svg" alt="youtube" /></div>
          <div className={styles.openBurger__social}><img src="/icons/open-burger-menu/telegram.svg" alt="telegram" /></div>
          <div className={styles.openBurger__social}><img src="/icons/open-burger-menu/whatsapp.svg" alt="whatsapp" /></div>
        </div>
      </div>
    </Layout>
  );
};

export default OpenBurger;