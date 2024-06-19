import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { Link } from 'react-router-dom';

import Input from '../../ui/input/Input';

import Slider from '../../slider/Slider';

import styles from './HomePage.module.scss';

const getData = async () => {
	const response = await axios.get('https://api.dev.zojnikfood.ru/api/food/', {
		headers: {
			'Content-Type': 'application/json',
		},
	});
	console.log(response);
	// const response = await fetch('https://api.dev.zojnikfood.ru/api/food/');

	return await response.data;
};

const HomePage = () => {
	const { data, error, isSuccess } = useQuery({
		queryKey: ['foods'],
		queryFn: getData,
	});

	console.log(data);

	return (
		<div className={styles.wrapper_homePage}>
			<Input />

			<div className={styles.block__methodPlate}>
				<div className={styles.block__text}>
					<h2>Метод тарелки</h2>
					<p>
						Выбирайте понравившиеся половинки тарелок, фильтруйте по тегам и
						анти-тегам
					</p>
				</div>
				<Link to='/constructor' className={styles.link}>
					Собрать тарелку
				</Link>
			</div>

			<Slider />
			<button onClick={getData}>TEST</button>
		</div>
	);
};

export default HomePage;
