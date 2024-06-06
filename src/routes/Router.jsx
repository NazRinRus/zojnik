import { BrowserRouter, Route, Routes } from 'react-router-dom';

import { routes } from './routes.data';

const Router = () => {
	return (
		<BrowserRouter>
			<Routes>
				{routes.map(route => {
					return (
						<Route
							key={route.path}
							element={<route.component />}
							path={route.path}
						/>
					);
				})}
				<Route element={<div>Not Found</div>} path='*' />
			</Routes>
		</BrowserRouter>
	);
};

export default Router;
