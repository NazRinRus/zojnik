import InterfaceApp from '../../ui/interface-app/InterfaceApp';

import Content from '../../content/Content';
import Header from '../../header/Header';
import Layout from '../../layout/Layout';

const Constructor = () => {
	return (
		<Layout>
			<Header title='Тарелка по Методу' />
			<Content />
			<InterfaceApp />
		</Layout>
	);
};

export default Constructor;
