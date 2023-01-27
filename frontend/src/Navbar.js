import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import logo from './logo.png'
import { useState,  useEffect } from 'react';
import axios from 'axios'


function BasicExample() {

  const [eventname, setEventName] = useState("")
  const local_event_name = 'http://127.0.0.1:5000/geteventname'
  const prod_event_name = 'https://dp-matchups.herokuapp.com/geteventname'

  useEffect(() => {
    axios
      .get(local_event_name)
      .then((res) => {
        setEventName(res.data)
      })
  }, [])

  return (
    <>
      <Navbar className="containerupper" bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">
            <img
              alt=""
              src={logo}
              width="120"
              height="120"
              className="d-inline-block align-center"
            />{' '}
            
          </Navbar.Brand>
          
          <Navbar.Collapse id="basic-navbar-nav">  
            <Nav className="me-auto">  
              <Nav.Link href="#home">Standings</Nav.Link>  
              <Nav.Link href="#about">Top 100</Nav.Link>  
            </Nav>  
          </Navbar.Collapse> 
        </Container>
      </Navbar>
      <br/>
      <Navbar className="containerlower" bg="dark" variant="dark">
        <Container className="containerlower">
          <div className="headername">Tournament: {eventname.name}</div>
        </Container>
      </Navbar>
    </>
  );
}

export default BasicExample;