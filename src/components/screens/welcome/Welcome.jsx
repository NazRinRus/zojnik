import { Link } from 'react-router-dom';

import Layout from '../../layout/Layout';

import styles from './Welcome.module.scss';

const Welcome = () => {
	return (
		<Layout>
			<img
				className={styles.welcome__background}
				src='./public/image/background/healthy_eating.svg'
				alt='healthy eating'
			/>
			<h1 className={styles.welcome__heading}>
				Начните свой ЗОЖ-путь сегодня!
			</h1>
			<p className={styles.welcome__text}>
				Заполните <Link className={styles.welcome__link}>АНКЕТУ ПРЕДПОЧТЕНИЙ,</Link> чтобы получить подборку блюд, идеально подходящих для вас
			</p>
			<Link to='/' className={styles.welcome__button}>
				Продолжить
			</Link>
		</Layout>
	);
};

export default Welcome;
