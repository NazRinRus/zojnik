import { Link } from 'react-router-dom';

import styles from './TitleAndBack.module.scss';

const TitleAndBack = ({ title }) => {
	return (
		<div className={styles.block__titleAndBack}>
			<Link to='/'>{'<'}</Link>
			<h1 className={styles.title}>{title}</h1>
			<div></div>
		</div>
	);
};

export default TitleAndBack;
