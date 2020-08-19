import React from 'react';
import Footer from './footer';
import {Link} from 'react-router-dom';
import './../styles/header.css';
import './../styles/todo.css';

const axios = require('axios');

/*The home page, that will show/create/delete/update tasks,
and redirect to others, such as Login and Register page.
*/
class Index extends React.Component{
  constructor(props){
    super(props);
    this.state = {todo: [], user: '', content: ''};
    this.logout = this.logout.bind(this);
    this.updateTask = this.updateTask.bind(this);
    this.createNewTask = this.createNewTask.bind(this);
    this.changeContent = this.changeContent.bind(this);
    this.createTask = this.createTask.bind(this);
    this.closePopUp = this.closePopUp.bind(this);
  }
  //Close Create Task Div
  closePopUp(){
    var popup = document.querySelector('.popUp');
    popup.style.display = "none";
  }
  //Set a state to task, to create it.
  changeContent(event){
    this.setState({content: event.target.value})
  }
  //Send content to API, with POST method, and add the content to task list
  createTask(){
    let params = {'content': this.state.content};
    axios.post("/api/createTask", params).then(res => {
      let newArray = this.state.todo;
      newArray.push({id: res.data, task: params.content, status: 0});
      this.setState({todo: newArray});
      this.setState({content: ''})
    })
    this.closePopUp();
  }
  createNewTask(){
    var popup = document.querySelector('.popUp');
    popup.style.display = "block";
  }
  //Update a task, the user clicks on task, and this will change the task status
  updateTask(id){
    axios.get(`/api/updateTask/${id}`).then(res => {
      if(res.data === 1){
        let todoList = this.state.todo;
        todoList.filter(element => element.id === id)[0].status = 
        (todoList.filter(element => element.id === id)[0].status === 0) ? 1 : 0;
        this.setState({todo: todoList});
      }
    })
  }
//Delete a task, the user clicks on task, and delete it.
  deleteTask(id){
    axios.get(`/api/deleteTask/${id}`).then(res => {
      if(res.data === 1){
        let todoList = this.state.todo.filter(element => element.id !== id);
        this.setState({todo: todoList});
      }
    })
  }
//Logou a user
  logout(){
    axios.get("/api/logout").then(res => {
      if(res.data !== "Not logged"){
        this.setState({user: ''});
        this.setState({todo: []})
      }
    });
  }
//When all components mount, front sends request to API, that return User and tasks to do.
  componentDidMount(){
    axios.get("/api/getuser").then(res => {
      if(res.data !== ""){
        this.setState({user: res.data});
      }
    });
    axios.get("/api/gettasks").then(res => {
      this.setState({todo: res.data});
    })
  }

  render(){
    return(
      <React.Fragment>
        <header className="topHeader">
          <h1>To Do List</h1>
          {this.state.user.length > 0 ?
            <React.Fragment>
              <h1 className = "option" id="userMenu">{this.state.user}
              <button onClick = {this.createNewTask}
              className="createTaskButton">Create Task</button></h1>
              <button onClick={() => this.logout()}>Logout</button>
            </React.Fragment>
          :
            <React.Fragment>
              <h1 className = "option"><Link to = "/register">Register</Link></h1>
              <h1 className = "option"><Link to="/login">Login</Link></h1>
            </React.Fragment>
          }
        </header>
        <div className = "content">
          <h2>Tasks</h2>
          <div className="todo">
            {this.state.todo.map((element, index) => {
              return(
                <React.Fragment>
                <div className="taskDiv" style={{animationDelay: (index * 100 ) + 'ms'}}>
                  <div className = "taskToDo">
                    <button className = "delete" onClick = {() => this.deleteTask(element.id)}>Delete</button>
                    <p>
                      {element.task}
                    </p>
                  </div>
                  {element.status === 1 ? 
                  <div className = "taskDone"><button onClick = {() => this.updateTask(element.id)}>Done</button></div> 
                  : <div className = "taskDoing"><button onClick = {() => this.updateTask(element.id)}>Doing...</button></div>}
                </div>
                </React.Fragment>
              )}
            )}
          </div>
        </div>
        <div className="popUp">
          <button className = "exitButton" onClick={this.closePopUp}>X</button>
          <h2>Create Your Task:</h2>
          <input type="text" value={this.state.content} onChange={this.changeContent}/>
          <button onClick = {this.createTask} className = "createButton">Create</button>
        </div>
        <Footer/>
      </React.Fragment>
    )
  }
}
export default Index;