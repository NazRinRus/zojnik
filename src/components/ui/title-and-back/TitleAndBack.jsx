import { Link, useNavigate } from 'react-router-dom';

import styles from './TitleAndBack.module.scss';

const TitleAndBack = ({ title }) => {
	const navigate = useNavigate();

	return (
		<div className={styles.block__titleAndBack}>
			{title === 'Салаты' || title === 'Белки и углеводы' ? (
				<button onClick={() => navigate(-1)}>{'<'}</button>
			) : (
				<Link to='/'>{'<'}</Link>
			)}
			<h1 className={styles.title}>{title}</h1>
			<div></div>
		</div>
	);
};

export default TitleAndBack;