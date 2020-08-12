import React from 'react';
import Header from './header';
import Footer from './footer';
import './../styles/todo.css';

const axios = require('axios');

class Index extends React.Component{
  constructor(props){
    super(props);
    this.state = {todo: []};
  }
  componentDidMount(){
    axios.get("/api/show").then(res => {
      this.setState({todo: res.data});
    })
  }
  render(){
    return(
      <React.Fragment>
        <Header/>
        <div className = "content">
          <h2>Tasks</h2>
          <div className="todo">
            {this.state.todo.map((element, index) => {
              return(
                <React.Fragment>
                <div className="taskDiv" id={'task' + index} key={index}>
                  <div className = "taskToDo">
                    <button className = "delete">Delete</button>
                    <p>
                      {element.content}
                    </p>
                  </div>
                  {element.status === 1 ? <div className = "taskDone"><button onClick = {() => this.undone(index)}>Done</button></div> : <div className = "taskDoing"><button onClick = {() => this.undone(index)}>Doing...</button></div>}
                </div>
                </React.Fragment>
              )}
            )}
          </div>
        </div>
        <Footer/>
      </React.Fragment>
    )
  }
}
export default Index;