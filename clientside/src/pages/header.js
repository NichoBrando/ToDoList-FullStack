import React from 'react';
import './../styles/header.css';

class Header extends React.Component{
  constructor(props){
    super(props);
    this.state = {user: ''};
  }
  render(){
    return (
      <React.Fragment>
        <header className="topHeader">
          <h1>To Do List</h1>
          {this.state.user.length > 0 ?
            <React.Fragment>
              <button>{this.state.user}</button>
              <button>Logout</button>
            </React.Fragment>
          :
            <React.Fragment>
              <button>Register</button>
              <button>Login</button>
            </React.Fragment>
          }
        </header>
      </React.Fragment>
    )
  }
}

export default Header