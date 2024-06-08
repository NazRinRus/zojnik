import { createSlice } from '@reduxjs/toolkit';

const initialState = {
	isViewBurger: false,
};

export const viewSettings = createSlice({
	name: 'viewSettings',
	initialState,
	reducers: {
		toggleBurger: (state, { payload }) => {
			state.isViewBurger = !state.isViewBurger;
		},
	},
});

export const { actions, reducer } = viewSettings;
