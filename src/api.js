import axios from 'axios';

const API_URL = 'http://api.dev.zojnikfood.ru';

export const $axios = axios.create({
	baseURL: API_URL,
	headers: {
		'Content-Type': 'application/json',
	},
});