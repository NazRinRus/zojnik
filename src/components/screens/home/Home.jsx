import InterfaceApp from '../../ui/interface-app/InterfaceApp';

import Content from '../../content/Content';
import Header from '../../header/Header';
import Layout from '../../layout/Layout';

const Home = () => {
	return (
		<Layout>
			<Header />
			<Content />
			<InterfaceApp />
		</Layout>
	);
};

export default Home;