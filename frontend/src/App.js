import {React} from 'react'
import {useForm} from 'react-hook-form';
import axios from 'axios'
import { useState,  useEffect } from 'react';
import Table from './Table';
import './tabledata.css';
import { NavLink, Routes, Route } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee, faCheck} from '@fortawesome/free-solid-svg-icons'
import BasicExample from './Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';

// const Main = () => (
//   <Switch>
//     <Route path='/about' component={About}></Route>
//   </Switch>
// );

const Home = () => (
  <div className='home'>
    <h1>Welcome to my portfolio website</h1>
    <p> Feel free to browse around and learn more about me.</p>
  </div>
);

const About = () => (
  <div className='about'>
    <h1>About Me</h1>
    <p>Ipsum dolor dolorem consectetur est velit fugiat. Dolorem provident corporis fuga saepe distinctio ipsam? Et quos harum excepturi dolorum molestias?</p>
    <p>Ipsum dolor dolorem consectetur est velit fugiat. Dolorem provident corporis fuga saepe distinctio ipsam? Et quos harum excepturi dolorum molestias?</p>
  </div>
);

const Contact = () => (
  <div className='contact'>
    <h1>Contact Me</h1>
    <p>You can reach me via email: <strong>hello@example.com</strong></p>
  </div>
);

const Main = () => (
  <Routes>
    <Route path='/' component={Home}></Route>
    <Route path='/about' component={About}></Route>
    <Route path='/contact' component={Contact}></Route>
  </Routes>
);

export default function App() {
  const { register, formState: { errors }, handleSubmit } = useForm();
  const [datapoints, setDataPoints] = useState("")
  const [eventname, setEventName] = useState("")
  const [sel_player, setSelPlayer] = useState("")
  const [loading, setLoading] = useState(false)
  const element = <FontAwesomeIcon icon="fa-solid fa-check" />
  
  let title = ""
  if (sel_player === "My") {
    title = " Players"

  } else {
    title = "'s Players"
  }

  const data2 = datapoints
  // axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
  // axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*';
  
  // const getHeadings = (datapoints) => {
  //   return Object.keys(datapoints[0]);
  // }
  
  const local = 'http://127.0.0.1:5000/matchups'
  const prod = 'https://dp-matchups.onrender.com/matchups'

  useEffect(() => {
    setLoading(true)
    axios
      .get(local + '?player=' + 'Matchups')
      .then((res) => {
        setLoading(false)
        setDataPoints(res.data)
        setSelPlayer('Matchups')
      })
  }, [])

  // useEffect(() => {
  //   axios
  //     .get(local_event_name)
  //     .then((res) => {
  //       setEventName(res.data)
  //     })
  // }, [])

  // const onSubmit = (data) => {
  //   const player_req = '?player=' + data.playername

    
  //   axios.get(local + player_req).then(res => {
      
  //     setDataPoints(res.data)
  //     setSelPlayer(data.playername)
  //     console.log(res.data)
  //   })
    
  //   console.log(data)

  //   axios.get(local_event_name).then(res => {
      
  //     setEventName(res.data)
  //     console.log(res.data)
  //   })
    

  // }

  return (

    
    <div>
      <Main></Main>
      {loading &&
        <div className='loaderdiv'>
          <p className="loadertext">Welcome to the: De Klopperij</p>
        </div>
      }
      {!loading &&
      <BasicExample></BasicExample>
      }
      {!loading && sel_player === "Matchups" && 
      // {sel_player === "Matchups" && 
        
        <div className='content'>
          {/* <h3>Tournament:</h3>
          <h3>{eventname.name}</h3> */}

          {data2.map((item, index) => {
            
            if (index === 0) {
              title = "Standings"
              return (
                <div className='table-elem standings' key={item}>
                <div className='customh1'>{title}</div>
                <div className='tablebodycustomstandings'>
                  <tr>
                      <th>Name</th>
                      <th>Points (Start)</th>
                      <th>Points</th>
                      <th>Movement</th>
                      <th>Total Diff</th>
                      <th>Total Points</th>
                  </tr>

                {item.map((player, index) => {
                  return (
                    <tr key={player}>
                      <td>{player.Name}</td>
                      <td>{player.StartPoints}</td>
                      <td>{player.Points}</td>
                      <td>{player.Movement}</td>
                      <td>{player.Difference}</td>
                      <td>{player.TotalPoints}</td>
                  </tr>

                  );
                })}

                </div>

                
              </div>
              )
            } else if (index ===1) {
              title = "Captains"
            } else {
              title = "Players"
            }
            
            
            return (
              
              <div className='table-elem' key={item}>
                <div className='customh1'>{title}</div>
                <div className='tablebodycustom'>
                  <tr className='trcustom'>
                      <th>Pos</th>
                      <th>Name</th>
                      <th>Today</th>
                      <th>Hole</th>
                      <th>Score</th>
                      <th>Martijn</th>
                      <th>Nicky</th>
                      <th>David</th>
                      <th>Johan</th>
                      <th>Jop</th>
                  </tr>

                {item.map((player, index) => {
                  return (
                    <tr key={player}>
                      <td>{player.position}</td>
                      <td>{player.name}</td>
                      <td>{player.scoretoday}</td>
                      <td>{player.onhole}</td>
                      <td>{player.score}</td>
                      <td>{player.Martijn && <FontAwesomeIcon icon={faCheck} color="rgb(34 197 94"/>}</td>
                      <td>{player.Nicky && <FontAwesomeIcon icon={faCheck} color="rgb(34 197 94"/>}</td>
                      <td>{player.David && <FontAwesomeIcon icon={faCheck} color="rgb(34 197 94"/>}</td>
                      <td>{player.Johan && <FontAwesomeIcon icon={faCheck} color="rgb(34 197 94"/>}</td>
                      <td>{player.Jop && <FontAwesomeIcon icon={faCheck} color="rgb(34 197 94"/>}</td>
                  </tr>

                  );
                })}

                </div>

                
              </div>
            );
          })}
          
        </div>
      }
      }
     </div>

  )
}
// export default function App() {

//   // const [data, setData] = useState([{}])
//   const {register, handleSubmit, errors} = useForm();

//   // useEffect(() => {
//   //   fetch("/matchups").then(
//   //     res => res.json()
//   //   ).then(
//   //     data => {
//   //       setData(data)
//   //       console.log(data)
//   //     }
//   //   )
//   // }, [])

//   return (


//     // <div>
//     <form>
//       <input type="text" placeholder="Player Name" name="player_name"/>
//       <input type="submit" />
//     </form>
//       // {(typeof data.players === 'undefined') ? (
//       //   <p>Loading...</p>
//       // ) : (
//       //   data.players.map((player, i) => (
//       //     <p key={i}>{player}</p>
//       //   ))

//       // )}



//     // </div>
//   )
// }