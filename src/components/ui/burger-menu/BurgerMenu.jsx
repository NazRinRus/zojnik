import styles from './BurgerMenu.module.scss';

const BurgerMenu = () => {
	return (
		<button className={styles.button__burger}>
			<div className={styles.burger}></div>
		</button>
	);
};

export default BurgerMenu;
