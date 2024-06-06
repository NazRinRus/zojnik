import BurgerMenu from '../ui/burger-menu/BurgerMenu';

import Geolocation from '../geolocation/Geolocation';

import styles from './Header.module.scss';

const Header = () => {
	return (
		<header className={styles.header}>
			<img src='./test_logo.png' alt='image' className={styles.logo} />
			<Geolocation />
			<BurgerMenu />
		</header>
	);
};

export default Header;
