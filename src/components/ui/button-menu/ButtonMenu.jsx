import { Link } from 'react-router-dom';
import styles from './ButtonMenu.module.scss';

const ButtonMenu = ({ id, path, leftIcon, rightIcon, title }) => {
  return (
    <Link key={id} to={path} className={styles.button__menu}>
      {leftIcon && (
        <img src={leftIcon} alt="icon" className={styles.button__menu__left__icon} />
      )}
      <span
        className={`${styles.button__menu__text}
        ${title === 'Выйти из аккаунта' ? styles.button__profile__logout : ''}`}>
        {title}
      </span>
      <img src={rightIcon} alt="arrow" className={styles.button__profile__right__icon} />
    </Link>
  );
};

export default ButtonMenu;