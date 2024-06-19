import { useState } from 'react';
import { Link } from 'react-router-dom';

import Button from '../../ui/button/Button';
import TitleAndBack from '../../ui/title-and-back/TitleAndBack';

import { colors } from '../../../app.constants';

import styles from './PlateConstructor.module.scss';
import AddToOrder from './add-to-order/AddToOrder';

const PlateConstructor = () => {
	const [isSpinning, setIsSpinning] = useState(false);

	const handleSpin = () => {
		setIsSpinning(true);
		setTimeout(() => {
			setIsSpinning(false);
		}, 600); // Длительность анимации в миллисекундах
	};

	return (
		<div className={styles.wrapper_constructor}>
			<TitleAndBack title='Тарелка по Методу' />
			<div className={styles.block__reload}>
				<img src='../icons/spin_the_plate.svg' alt='spin_the_plate' />
				<button className={styles.button__reload} onClick={handleSpin}>
					Покрутите тарелку
				</button>
			</div>
			<div
				className={`${styles.block__plate} ${isSpinning ? styles.spin : ''}`}
				style={{ position: 'relative' }}
			>
				<div className={styles.block__left}>
					<Link to='/protein' className={styles.block__image}>
						<img src='./icons/add.svg' alt='add' />
					</Link>
				</div>
				<div
					className={styles.block__right}
					style={{
						position: 'absolute',
						left: '0',
						top: '0',
					}}
				>
					<Link
						to='/salads'
						className={`${styles.block__image} ${styles.right}`}
					>
						<img src='./icons/add.svg' alt='add' />
					</Link>
				</div>

				{/* <img src='../image/plate_one.png' alt='plate' />
				<img
					src='../image/plate_two.png'
					alt='plate'
					style={{
						position: 'absolute',
						left: '0',
						top: '0',
					}}
				/> */}
				<p className={styles.help}>
					Соберите в конструкторе свою <br></br> идеальную тарелку
				</p>
			</div>
			<Button
				style={{
					back: colors.color_grey_disable,
					color: colors.color_white,
				}}
			>
				В корзину
			</Button>
			<AddToOrder />
		</div>
	);
};

export default PlateConstructor;
