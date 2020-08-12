import React from 'react';
import {BrowserRouter, Link, Switch} from 'react-router-dom';
import Index from './pages/todo';

const Routes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Link to = "/" exact component={Index}/>
        <Link to = "/register" exact />
        <Link to = "/login" exact />
        <Link to = "/tasks" exact />
      </Switch>
    </BrowserRouter>
  )
}

export default Routes;