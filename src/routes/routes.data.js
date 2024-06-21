import Authorization from '../components/screens/authorization/Authorization';
import Constructor from '../components/screens/constructor/Constructor';
import Home from '../components/screens/home/Home';
import Profile from '../components/screens/profile/Profile';
import Protein from '../components/screens/protein/Protein';
import Salads from '../components/screens/salads/Salads';
import Welcome from '../components/screens/welcome/Welcome';

import OpenBurgerMenu from '../components/open-burger/OpenBurger';

export const routes = [
	{
		path: '/',
		component: Home,
		isAuth: false,
	},
	{
		path: '/welcome',
		component: Welcome,
		isAuth: false,
	},
	{
		path: '/constructor',
		component: Constructor,
		isAuth: false,
	},
	{
		path: '/profile',
		component: Profile,
		isAuth: false,
	},
	{
		path: '/authorization',
		component: Authorization,
		isAuth: false,
	},
	{
		path: '/salads',
		component: Salads,
		isAuth: false,
	},
	{
		path: '/protein',
		component: Protein,
		isAuth: false,
	},
  {
		path: '/test',
		component: OpenBurgerMenu,
		isAuth: false,
	}
];
