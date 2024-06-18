import Constructor from '../components/screens/constructor/Constructor';
import Home from '../components/screens/home/Home';
import Welcome from '../components/screens/welcome/Welcome';
import Profile from '../components/screens/profile/Profile';
import Authorization from '../components/screens/authorization/Authorization';

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
];
