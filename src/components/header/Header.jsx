import BurgerMenu from '../ui/burger-menu/BurgerMenu';

import Geolocation from '../geolocation/Geolocation';

import styles from './Header.module.scss';

<<<<<<< HEAD
const Header = ({ title }) => {
  return (
    <header className={styles.header}>
      <>
        {title === 'Вход или регистрация' ? (
          <>
            <div></div>
            <h1 className={styles.header__title}>{title}</h1>
            <img src="./icons/close menu burger.svg" alt="close" />
          </>
        ) : title ? (
          <>
            <Link to='/'>{'<'}</Link>
            <h1 className={styles.header__title}>{title}</h1>
            <BurgerMenu />
          </>
        ) : (
          <>
            <img src='./logo.svg' alt='image' className={styles.logo} />
            <Geolocation />
            <BurgerMenu />
          </>
        )}
      </>
    </header>
  );
=======
const Header = () => {
	return (
		<header className={styles.header}>
			<img src='./test_logo.png' alt='image' className={styles.logo} />
			<Geolocation />
			<BurgerMenu />
		</header>
	);
>>>>>>> f5e0d7b9ea415895783096675815dce4b0942346
};

export default Header;
