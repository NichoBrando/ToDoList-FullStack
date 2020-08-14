import React from 'react';
import './../styles/form.css';

const axios = require('axios');

class Login extends React.Component{
  constructor(props){
    super(props);
    this.state = {username: '', password: ''};
    this.changeUsername = this.changeUsername.bind(this);
    this.changePassword = this.changePassword.bind(this);
    this.checkForm = this.checkForm.bind(this);
  }
  changeUsername(event){
    this.setState({username: event.target.value})
  }
  changePassword(event){
    this.setState({password: event.target.value})
  }
  checkForm(){
    let params = {username: this.state.username, password: this.state.password};
    if(params.username.length > 4 && params.password.length > 4){
      axios.post("/api/login", params).then(res => {
        alert(res.data)
        if(res.data === "Sucess! Redirectioning..."){
          window.location.replace("/");
        }
      });
    }
    else{
      alert("invalid username or password")
    }
  }
  render(){
    return(
      <React.Fragment>
        <div className="waveOverflow">
          <svg className = "top" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="blue" fill-opacity="1" d="M0,128L26.7,133.3C53.3,139,107,149,160,154.7C213.3,160,267,160,320,138.7C373.3,117,427,75,480,85.3C533.3,96,587,160,640,197.3C693.3,235,747,245,800,234.7C853.3,224,907,192,960,202.7C1013.3,213,1067,267,1120,266.7C1173.3,267,1227,213,1280,202.7C1333.3,192,1387,224,1413,240L1440,256L1440,0L1413.3,0C1386.7,0,1333,0,1280,0C1226.7,0,1173,0,1120,0C1066.7,0,1013,0,960,0C906.7,0,853,0,800,0C746.7,0,693,0,640,0C586.7,0,533,0,480,0C426.7,0,373,0,320,0C266.7,0,213,0,160,0C106.7,0,53,0,27,0L0,0Z"></path></svg>        
          <svg className = "bottom" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="blue" fill-opacity="1" d="M0,128L26.7,133.3C53.3,139,107,149,160,154.7C213.3,160,267,160,320,138.7C373.3,117,427,75,480,85.3C533.3,96,587,160,640,197.3C693.3,235,747,245,800,234.7C853.3,224,907,192,960,202.7C1013.3,213,1067,267,1120,266.7C1173.3,267,1227,213,1280,202.7C1333.3,192,1387,224,1413,240L1440,256L1440,320L1413.3,320C1386.7,320,1333,320,1280,320C1226.7,320,1173,320,1120,320C1066.7,320,1013,320,960,320C906.7,320,853,320,800,320C746.7,320,693,320,640,320C586.7,320,533,320,480,320C426.7,320,373,320,320,320C266.7,320,213,320,160,320C106.7,320,53,320,27,320L0,320Z"></path></svg>     
          <div className="form">
            <h1>Login</h1>
            <input type="text" value = {this.state.username} onChange = {this.changeUsername} placeholder="Username"/>
            <input type="password" value = {this.state.password} onChange = {this.changePassword} placeholder="Password"/>
            <button onClick={this.checkForm}>Register</button>
          </div>
        </div>
      </React.Fragment>
    )
  }
}

export default Login;