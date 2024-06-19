import { useLocation } from 'react-router-dom';

import styles from './Content.module.scss';
import HomePage from './home-page/HomePage';
import PlateConstructor from './plate-constructor/PlateConstructor';
import Products from './products/Products';

const Content = () => {
	const { pathname } = useLocation();

	return (
		<div className={styles.block__content}>
			{pathname === '/' ? (
				<HomePage />
			) : pathname === '/salads' ? (
				<Products title='Салаты' />
			) : pathname === '/protein' ? (
				<Products title='Белки и углеводы' />
			) : (
				<PlateConstructor />
			)}
		</div>
	);
};

export default Content;
