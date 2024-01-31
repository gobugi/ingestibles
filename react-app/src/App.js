import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar/NavBar';
import Homepage from './components/Homepage/Homepage';
import MyPlate from './components/MyPlate/MyPlate';
import ProtectedRoute from './components/auth/ProtectedRoute';
import CreateRecipe from './components/CreateRecipe/CreateRecipe';
import { authenticate } from './store/session';
import SingleRecipePage from './components/SingleRecipePage';
import Profile from "./components/Profile/profile";
import EditRecipe from "./components/EditRecipe/EditRecipe"
import Recipes from './components/Recipes/Recipes';
import Footer from './components/Footer/Footer';

const ScrollToTop = (props) => {
  const location = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location]);

  return <>{props.children}</>;
};


function App() {
	const [loaded, setLoaded] = useState(false);
	const dispatch = useDispatch();

	useEffect(() => {
		(async () => {
			await dispatch(authenticate());
			setLoaded(true);
		})();
	}, [dispatch]);

	if (!loaded) {
		return null;
	}

	return (
    <BrowserRouter>
      <NavBar loaded={loaded} />
      {loaded && (
        <ScrollToTop>
          <Switch>
            <Route path="/" exact={true}>
              <Homepage />
            </Route>
            <Route path="/login" exact={true}>
              <LoginForm />
            </Route>
            <Route path="/sign-up" exact={true}>
              <SignUpForm />
            </Route>
            <ProtectedRoute path="/recipes/my_plate" exact={true}>
              <MyPlate />
            </ProtectedRoute>
            <ProtectedRoute path="/users/:userId" exact={true}>
              <Profile />
            </ProtectedRoute>
            <ProtectedRoute path="/recipes/new_recipe" exact={true}>
              <CreateRecipe />
            </ProtectedRoute>
            <ProtectedRoute path="/recipes/edit/:recipeId" exact={true}>
              <EditRecipe />
            </ProtectedRoute>
            <ProtectedRoute path="/" exact={true}>
              <h1>My Home Page</h1>
            </ProtectedRoute>
            <Route path="/recipes/:recipeId" exact={true}>
              <SingleRecipePage />
            </Route>
            <Route path="/recipes" exact={true}>
              <Recipes />
            </Route>
            <Route path="/tags/:tagName" exact={true}>
              <Recipes />
            </Route>
          </Switch>
        </ScrollToTop>
      )}
      <Footer />
    </BrowserRouter>
  );
}

export default App;
