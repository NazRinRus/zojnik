import Layout from '../../layout/Layout';
import Header from '../../header/Header';
import InputPhone from '../../ui/input-phone/InputPhone';
import ButtonAdd from '../../ui/button-add/ButtonAdd';

import styles from '../authorization/Authorization.module.scss';

const Authorization = () => {
  return (
    <Layout>
      <Header
        title='Вход или регистрация'
      />
      <div className={styles.authorization}>
        <p className={styles.authorization__text}>Для входа или регистрации укажите номер телефона</p>
        <div className={styles.authorization__phone}>
          <InputPhone />
          <div className={styles.authorization__agreement}>
            <label className={styles.authorization__checkbox_container}>
              <input type="checkbox" />
              <span className={styles.authorization__checkmark}></span>
            </label>
            <p className={styles.authorization__agreement__text}>Соглашаюсь с Политикой конфеденциальности и Пользовательским соглашением</p>
          </div>
        </div>
        <ButtonAdd
          text='Получить код по SMS'
        />
      </div>
    </Layout>
  );
};

export default Authorization;