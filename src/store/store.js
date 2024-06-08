import { combineReducers, configureStore } from '@reduxjs/toolkit';

import { reducer as viewSettings } from './view-settings/viewSettings.slice';

const reducers = combineReducers({
	viewSettings,
});

export const store = configureStore({
	reducer: reducers,
});
