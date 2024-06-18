import InputMask from 'react-input-mask';
import styles from './InputPhone.module.scss';

const InputPhone = () => {

	return (
    <div className={styles.input__block}>
      <label htmlFor="phone" className={styles.input__phone}>Телефон</label>
      <InputMask
        mask='+7 (999) 999-99-99'
        placeholder='+7 ('
        className={styles.input__phone__add}
      />
    </div>
	);
};

export default InputPhone;
