import React from 'react';
import './../styles/footer.css';

class Footer extends React.Component{
  render(){
    return (
      <React.Fragment>
        <footer className="Footer">
          <h3>To Do List</h3>
          <div className = "footerContents">
            <div className = "author">
              <p>Created by: Nicholas Brandão.</p>
              <p>Full Stack Developer.</p>
            </div>
            <div className = "contacts">
              <ul>
                <li><a href = "https://github.com/NichoBrando" >
                  GitHub</a></li>
                <li><a href = "https://www.linkedin.com/in/nicholas-brandao-developer/">
                  LinkedIn</a></li>
              </ul>
            </div>
            <div className = "aboutProject">
              <p>This project was made to show my experience
                with ReactJS and Flask as API.
              </p>
            </div>
          </div>
        </footer>
      </React.Fragment>
    )
  }
}

export default Footer;