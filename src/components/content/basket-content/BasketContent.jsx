import { Link } from 'react-router-dom';

import TitleAndBack from '../../ui/title-and-back/TitleAndBack';

import { useBasket } from '../../../hooks/useBasket';

import AddToOrder from '../plate-constructor/add-to-order/AddToOrder';

import styles from './BasketContent.module.scss';
import ProductInBasket from './product-in-basket/ProductInBasket';

const BasketContent = () => {
	const { basketProducts, setBasketProducts } = useBasket();

	return (
		<>
			{basketProducts ? (
				<div className={styles.wrapper_basket}>
					<>
						<TitleAndBack title='Корзина' />
						<img
							src='/image/basket.png'
							alt='basket'
							className={styles.image}
						/>
						<h2 className={styles.title}>Корзина пока пуста</h2>
						<p className={styles.error}>
							Здесь будут блюда, которые вы добавите в корзину
						</p>
						<Link to='/catalog' className={styles.link}>
							Перейти в каталог
						</Link>
					</>
				</div>
			) : (
				<div className={styles.wrapper_basketProducts}>
					<ProductInBasket />
					<AddToOrder />
				</div>
			)}
		</>
	);
};

export default BasketContent;
