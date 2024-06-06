import { Link } from 'react-router-dom';

import styles from './InterfaceApp.module.scss';
import { arrayInterfaceApp } from './inteface.data';

const InterfaceApp = () => {
	return (
		<div className={styles.block__interface}>
			{arrayInterfaceApp.map(icon => (
				<Link to={icon.path} key={icon.id} className={styles.list}>
					<img src={icon.src} alt='img' className={styles.image} />
				</Link>
			))}
		</div>
	);
};

export default InterfaceApp;
