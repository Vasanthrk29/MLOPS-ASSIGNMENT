import React, { useState } from 'react';
import axios from 'axios';
import './styles.css'; // Import the CSS file

function App() {
  const [square_Meters, setsquare_Meters] = useState('');
  const [number_Of_Rooms, setnumber_Of_Rooms] = useState('');
  const [city_Part_Range, setcity_Part_Range] = useState('');
  const [num_Prev_Owners, setnum_Prev_Owners] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleInputChange = (e, setInputFunction) => {
    setInputFunction(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/', {
        squareMeters: square_Meters,
        numberOfRooms: number_Of_Rooms,
        cityPartRange: city_Part_Range,
        numPrevOwners: num_Prev_Owners
      });
      setOutput(response.data.output);
      setError('');
    } catch (error) {
      console.error('Error:', error);
      setError('Error: Something went wrong. Please try again.');
      setOutput('');
    }
  };

  return (
    <div className="container">
      <h1>Paris house price prediction</h1>
      <form onSubmit={handleSubmit} className="form">
        <div className="input-group">
          <label>square_Meters:</label>
          <input type="text" value={square_Meters} onChange={(e) => handleInputChange(e, setsquare_Meters)} />
        </div>
        <div className="input-group">
          <label>number_Of_Rooms:</label>
          <input type="text" value={number_Of_Rooms} onChange={(e) => handleInputChange(e, setnumber_Of_Rooms)} />
        </div>
        <div className="input-group">
          <label>city_Part_Range:</label>
          <input type="text" value={city_Part_Range} onChange={(e) => handleInputChange(e, setcity_Part_Range)} />
        </div>
        <div className="input-group">
          <label>num_Prev_Owners:</label>
          <input type="text" value={num_Prev_Owners} onChange={(e) => handleInputChange(e, setnum_Prev_Owners)} />
        </div>
        <button type="submit" className="button">Submit</button>
      </form>
      {error && <div style={{ color: 'red', marginTop: '10px' }}>{error}</div>}
      {output && <div style={{ marginTop: '10px' }}>House price: {output}</div>}
    </div>
  );
}

export default App;
