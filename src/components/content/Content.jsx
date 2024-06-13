import { useLocation } from 'react-router-dom';

import styles from './Content.module.scss';
import HomePage from './home-page/HomePage';
import PlateConstructor from './plate-constructor/PlateConstructor';

const Content = () => {
	const { pathname } = useLocation();

	return (
		<div className={styles.block__content}>
			{pathname === '/' ? <HomePage /> : <PlateConstructor />}
		</div>
	);
};

export default Content;
