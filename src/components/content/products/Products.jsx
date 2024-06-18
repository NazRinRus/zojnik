import Input from '../../ui/input/Input';
import TitleAndBack from '../../ui/title-and-back/TitleAndBack';

import { useFoods } from '../../../hooks/useFoods';

import styles from './Products.module.scss';

const Products = ({ title }) => {
	const { data } = useFoods();

	console.log(data);
	return (
		<div className={styles.wrapper_product}>
			<Input />
			<TitleAndBack title={title} />
		</div>
	);
};

export default Products;
