import { Link } from 'react-router-dom';

import { arrayButtonProfile } from './buttonsProfile.data';
import styles from './ButtonsProfile.module.scss';

const ButtonsProfile = () => {
  return(
    <div className={styles.buttons_wrapper_profile}>
      {arrayButtonProfile.map(button => (
        <div key={button.id} className={styles.button_profile}>
          <Link to={button.path} className={styles.button_profile__link}>
            {button.leftIcon && (
              <img src={button.leftIcon} alt="icon" className={styles.button_profile_left__icon} />
            )}
            <span
              className={`${styles.button_profile__text}
              ${button.title === 'Выйти из аккаунта' ? styles.button_profile__text_logout : ''}`}>
              {button.title}
            </span>
            <img src={button.rightIcon} alt="arrow" className={styles.button_profile_right__icon} />
          </Link>
        </div>
      ))}
    </div>
  );
};

export default ButtonsProfile;