import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import Index from './pages/todo';
import Login from './pages/login';
import Register from './pages/register';

/*Organize the views with routes, each route have a function
in this project*/
const Routes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path = "/" exact component={Index}/>
        <Route path = "/register" exact component={Register}/>
        <Route path = "/login" exact component={Login}/>
      </Switch>
    </BrowserRouter>
  )
}

export default Routes;