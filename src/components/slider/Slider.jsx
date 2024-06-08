import { Link } from 'react-router-dom';

import styles from './Slider.module.scss';
import { categoryFood } from './slider.data';

const Slider = () => {
	return (
		<div className={styles.block__slider}>
			{categoryFood.map(elem => (
				<Link className={styles.block__category}>
					{/* <img src="" alt="" /> */}
					<p>{elem.title}</p>
				</Link>
			))}
		</div>
	);
};

export default Slider;
