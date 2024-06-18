<<<<<<< HEAD
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
=======
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';
import { VitePWA } from 'vite-plugin-pwa';
>>>>>>> f5e0d7b9ea415895783096675815dce4b0942346

export default defineConfig({
<<<<<<< HEAD
  plugins: [react()],
=======
	plugins: [
		react(),
		VitePWA({
			registerType: 'autoUpdate',
			manifest: {
				name: 'Healthy Food App',
				short_name: 'HealthyFood',
				description: 'An app for healthy food recipes',
				theme_color: '#ffffff',
				icons: [
					{
						src: '/icons8-green-apple-96_192x192.png',
						sizes: '192x192',
						type: 'image/png',
					},
					{
						src: '/icons8-green-apple-96_1_512x512.png',
						sizes: '512x512',
						type: 'image/png',
					},
				],
			},
		}),
	],
>>>>>>> f5e0d7b9ea415895783096675815dce4b0942346
});
