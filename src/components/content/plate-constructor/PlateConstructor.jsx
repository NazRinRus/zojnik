import { useState } from 'react';

import styles from './PlateConstructor.module.scss';

const PlateConstructor = () => {
	const [isSpinning, setIsSpinning] = useState(false);

	const handleSpin = () => {
		setIsSpinning(true);
		setTimeout(() => {
			setIsSpinning(false);
		}, 2000); // Длительность анимации в миллисекундах
	};

	return (
		<div className={styles.wrapper_constructor}>
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
					<div className={styles.block__image}>
						<img src='./icons/add.svg' alt='add' />
					</div>
				</div>
				<div
					className={styles.block__right}
					style={{
						position: 'absolute',
						left: '0',
						top: '0',
					}}
				>
					<div className={`${styles.block__image} ${styles.right}`}>
						<img src='./icons/add.svg' alt='add' />
					</div>
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
		</div>
	);
};

export default PlateConstructor;
