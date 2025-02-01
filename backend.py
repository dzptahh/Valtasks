from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import json
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app first
app = FastAPI()

# Mount static folder after app initialization
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define Ability and Agent models
class Ability(BaseModel):
    name: str
    effect: str
    cooldown: int  # Cooldown in seconds

class Agent(BaseModel):
    name: str
    role: str
    health: int
    image_url: str  # This will point to a static file
    abilities: List[Ability]

# Middleware for handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Valorant Agent API! Visit /docs for interactive API documentation."}

# Load agent data from JSON file
def load_agents_data(file_path: str):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [Agent(**agent) for agent in data]

# Load agents data (assumes the file is in the same directory as the app)
agents_data = load_agents_data("agents_data.json")

# API to get all agents or filter by role and ability
@app.get("/agents/", response_model=List[Agent])
async def get_agents(role: str = None, ability: str = None):
    filtered_agents = agents_data

    if role:
        filtered_agents = [agent for agent in filtered_agents if agent.role.lower() == role.lower()]

    if ability:
        filtered_agents = [agent for agent in filtered_agents if any(ab.name.lower() == ability.lower() for ab in agent.abilities)]

    return filtered_agents

# API to get a specific agent by name
@app.get("/agents/{agent_name}", response_model=Agent)
async def get_agent(agent_name: str):
    agent = next((a for a in agents_data if a.name.lower() == agent_name.lower()), None)
    return {"error": "Agent not found"} if agent is None else agent

@app.post("/use_ability/{agent_name}/{ability_name}")
async def use_ability(agent_name: str, ability_name: str):
    agent = next((a for a in agents_data if a.name.lower() == agent_name.lower()), None)
    if agent is None:
        return {"error": "Agent not found"}

    ability = next((ab for ab in agent.abilities if ab.name.lower() == ability_name.lower()), None)
    if ability is None:
        return {"error": "Ability not found"}

    if ability.cooldown == 0:
        return {"message": f"{ability.name} is ready to use!"}
    else:
        return {"message": f"{ability.name} is on cooldown for {ability.cooldown} seconds."}

@app.post("/level_up/{agent_name}")
async def level_up(agent_name: str):
    agent = next((a for a in agents_data if a.name.lower() == agent_name.lower()), None)
    if agent is None:
        return {"error": "Agent not found"}

    agent.health += 20  # Increase health by 20 for each level
    return {"message": f"{agent.name} leveled up! New health: {agent.health}"}
