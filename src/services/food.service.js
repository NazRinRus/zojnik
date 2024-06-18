import { $axios } from '../api';

export const foodService = {
	getData: async () => {
		const response = await $axios.get('/api/food/');
		// const response = await fetch('https://api.dev.zojnikfood.ru/api/food/');

		return await response.data;
	},
};
