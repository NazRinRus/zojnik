import styles from './Button.module.scss';

const Button = ({ children, style }) => {
	const styleButton = {
		backgroundColor: style.back,
		color: style.color,
	};

	return (
		<button className={styles.button} style={styleButton}>
			{children}
		</button>
	);
};

export default Button;
