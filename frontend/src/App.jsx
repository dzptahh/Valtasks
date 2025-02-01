import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [agents, setAgents] = useState([]);
  const [selectedAgent, setSelectedAgent] = useState(null);

  // Fetch agents data
  const fetchAgents = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/agents/');
      const data = await response.json();
      setAgents(data);
    } catch (error) {
      console.error('Error fetching agents:', error);
    }
  };

  useEffect(() => {
    fetchAgents();
  }, []);

  const handleAgentClick = (agent) => {
    setSelectedAgent(agent);
  };

  return (
    <div className="App">
      <h1>Valorant Agents</h1>

      <h2>Available Agents</h2>
      <div>
        {agents.length > 0 ? (
          <ul>
            {agents.map((agent) => (
              <li key={agent.name} onClick={() => handleAgentClick(agent)}>
                {agent.name}
              </li>
            ))}
          </ul>
        ) : (
          <p>No agents available</p>
        )}
      </div>

      {selectedAgent && (
        <div className="agent-details">
          <h3>{selectedAgent.name}</h3>
          <p><strong>Role:</strong> {selectedAgent.role}</p>
          <p><strong>Health:</strong> {selectedAgent.health}</p>
          <h4>Abilities:</h4>
          <ul>
            {selectedAgent.abilities.map((ability) => (
              <li key={ability.name}>
                <strong>{ability.name}</strong>: {ability.effect} (Cooldown: {ability.cooldown}s)
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
