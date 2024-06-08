import Constructor from '../components/screens/constructor/Constructor';
import Home from '../components/screens/home/Home';
import Welcome from '../components/screens/welcome/Welcome';

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
];
