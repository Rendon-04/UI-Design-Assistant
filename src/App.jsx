import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Import the CSS file

function App() {
  const [query, setQuery] = useState(''); // User input
  const [componentCode, setComponentCode] = useState(''); // AI-generated component

  const handleSearch = async () => {
    try {
      // Send the query to the Flask backend
      const response = await axios.post('http://localhost:5000/generate', { query });
      setComponentCode(response.data.componentCode); // Set the generated component code
    } catch (error) {
      console.error('Error generating component:', error);
      setComponentCode('Error generating component. Please try again.');
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">UI Design Assistant</h1>
      <div className="search-container">
        <input
          type="text"
          placeholder="Enter a component description..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="search-input"
        />
        <button onClick={handleSearch} className="generate-button">
          Generate Component
        </button>
      </div>
      <div className="output-container">
        <h2 className="output-title">Generated Component Code:</h2>
        <pre className="output-preview">
          {componentCode || 'Your generated component will appear here.'}
        </pre>
      </div>
    </div>
  );
}

export default App;
