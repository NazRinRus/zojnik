import { Link } from 'react-router-dom';

import styles from './ButtonAdd.module.scss';

const ButtonAdd = ({text}) => {
  return (
    <Link>
      <button className={styles.button__add}>{text}</button>
    </Link>
  );
};

export default ButtonAdd;