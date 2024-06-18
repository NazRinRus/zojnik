import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';

import Router from './routes/Router.jsx';
import { store } from './store/store.js';
import './styles/global.scss';
<<<<<<< HEAD
=======

if ('serviceWorker' in navigator) {
	window.addEventListener('load', () => {
		navigator.serviceWorker
			.register('/service-worker.js')
			.then(registration => {
				console.log('SW registered: ', registration);
			})
			.catch(registrationError => {
				console.log('SW registration failed: ', registrationError);
			});
	});
}
>>>>>>> f5e0d7b9ea415895783096675815dce4b0942346

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<Provider store={store}>
			<Router />
		</Provider>
	</React.StrictMode>,
);
