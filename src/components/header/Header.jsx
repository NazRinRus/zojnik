import BurgerMenu from '../ui/burger-menu/BurgerMenu';

import Geolocation from '../geolocation/Geolocation';

import styles from './Header.module.scss';

const Header = () => {
	return (
		<header className={styles.header}>
			{/* {title ? (
				<>
					<Link to='/'>{'<'}</Link>
					<h1 className={styles.header__title}>{title}</h1>
				</>
			) : (
				<>
					<img src='./test_logo.png' alt='image' className={styles.logo} />
					<Geolocation />
				</>
			)} */}
			<img src='./test_logo.png' alt='image' className={styles.logo} />
			<Geolocation />
			<BurgerMenu />
		</header>
	);
};

export default Header;
