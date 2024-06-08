import { useLocation } from 'react-router-dom';

import Input from '../ui/input/Input';

import Slider from '../slider/Slider';

import styles from './Content.module.scss';
import PlateConstructor from './plate-constructor/PlateConstructor';

const Content = () => {
	const { pathname } = useLocation();

	return (
		<div className={styles.block__content}>
			{pathname === '/' ? (
				<>
					<Input />
					<Slider />{' '}
				</>
			) : (
				<PlateConstructor />
			)}
		</div>
	);
};

export default Content;
