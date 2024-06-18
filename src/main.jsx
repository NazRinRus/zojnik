import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import React from 'react';
import ReactDOM from 'react-dom/client';

import Router from './routes/Router.jsx';
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

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<QueryClientProvider client={queryClient}>
			<Router />
			<ReactQueryDevtools initialIsOpen={false} />
		</QueryClientProvider>
	</React.StrictMode>,
);
