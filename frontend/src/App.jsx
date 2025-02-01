import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [agents, setAgents] = useState([]);
  const [selectedAgent, setSelectedAgent] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch agents data
  const fetchAgents = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/agents/');
      if (!response.ok) {
        throw new Error('Failed to fetch agents');
      }
      const data = await response.json();
      setAgents(data);
    } catch (error) {
      console.error('Error fetching agents:', error);
      setError(error.message);
    } finally {
      setIsLoading(false);
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
      <h1>Valorant <span>Agents</span></h1>
      <h2>Available Agents</h2>

      {isLoading && <p>Loading agents...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      <div className="agent-container">
        {/* Agent List */}
        <div className="agents-list">
          {agents.length > 0 ? (
            <ul>
              {agents.map((agent) => (
                <li
                  key={agent.id}
                  onClick={() => handleAgentClick(agent)}
                  style={{ cursor: 'pointer' }}
                >
                  <img
                    src={`http://127.0.0.1:8000/static/images/${agent.image_url}`}
                    alt={agent.name}
                    className="agent-image"
                  />
                  <p>{agent.name}</p>
                </li>
              ))}
            </ul>
          ) : (
            <p>No agents available</p>
          )}
        </div>

        {/* Agent Details */}
        {selectedAgent && (
          <div className="agent-details">
            <div className="agent-name-image">
              <img
                src={`http://127.0.0.1:8000/static/images/${selectedAgent.image_url}`}
                alt={selectedAgent.name}
                className="agent-image-background"
              />
              <h3 className="agent-name">{selectedAgent.name}</h3>
            </div>
            <p><strong>Role:</strong> {selectedAgent.role}</p>
            <p><strong>Health:</strong> {selectedAgent.health}</p>

            {selectedAgent.abilities && selectedAgent.abilities.length > 0 ? (
              <div className="abilities-list">
                {selectedAgent.abilities.map((ability, index) => (
                  <div className="ability-card" key={index}>
                    <h5>{ability.name}</h5>
                    <p className="ability-effect">{ability.effect}</p>
                    <p className="ability-description">{ability.description}</p>
                    <p><strong>Cooldown:</strong> {ability.cooldown}s</p>
                  </div>
                ))}
              </div>
            ) : (
              <p>No abilities available for this agent.</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
