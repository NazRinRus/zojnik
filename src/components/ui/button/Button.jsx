import { useNavigate } from 'react-router-dom';

import styles from './Button.module.scss';

const Button = ({ children, style, buttonFor }) => {
	const navigate = useNavigate();
	const styleButton = {
		backgroundColor: style.back,
		color: style.color,
	};

	const onClick = () => {
		navigate('/basket');
	};

	return (
		<button
			className={styles.button}
			style={styleButton}
			onClick={() => (buttonFor === 'go-basket' ? onClick() : undefined)}
		>
			{children}
		</button>
	);
};

export default Button;
