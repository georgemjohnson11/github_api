import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './containers/Home';
// import { Provider } from 'react-redux';
// import store from './store';
const App = () => (
    // <Provider store={store}>
        <Router>
            <Switch>
                <Route exact path='/' component={Home} />
            </Switch>
        </Router>
    // </Provider>
);

export default App;