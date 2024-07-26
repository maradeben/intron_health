import React, {useEffect, useState} from 'react';
import './App.css';

function App() {

  const [data, setData] = useState(0)

  useEffect (() => {
    fetch("http://localhost:5000/doctors/1").then(res => res.json()).then(data => {
        console.log(data)
        setData(data.result);
        console.log('data', data.result);
      });
  }, []);

return (
    <div className="App">
  {/* //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.tsx</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //     </header> */}
          <h1>In progress</h1>
          <p>{data}</p>
    </div>
  );
}

export default App;
