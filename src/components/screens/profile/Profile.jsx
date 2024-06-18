import Layout from '../../layout/Layout';
import Header from '../../header/Header';
import InterfaceApp from '../../ui/interface-app/InterfaceApp';
import ButtonMenu from '../../ui/button-menu/ButtonMenu';

import { arrayButtonProfile } from '../../screens/profile/buttonsProfile.data';
import styles from './Profile.module.scss';


const Profile = () => {
  return (
    <Layout>
      <Header />
      <div className={styles.avatar__profile}>
        <div className={styles.avatar__profile__image}>
          <img src="/icons/profile/avatar.svg" alt="avatar" />
        </div>
      </div>
      <div className={styles.buttons__wrapper__profile}>
        {arrayButtonProfile.map(button => (
          <ButtonMenu
            key={button.id}
            id={button.id}
            path={button.path}
            leftIcon={button.leftIcon}
            rightIcon={button.rightIcon}
            title={button.title}
          />
        ))}
      </div>
      <InterfaceApp />
    </Layout>
  );
};

export default Profile;