import { createContext, useState } from 'react';

export const BasketContext = createContext();

const BasketProvider = ({ children }) => {
	const [basketProducts, setBasketProducts] = useState();

	return (
		<BasketContext.Provider value={{ basketProducts, setBasketProducts }}>
			{children}
		</BasketContext.Provider>
	);
};

export default BasketProvider;
