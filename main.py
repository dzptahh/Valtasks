# main.py
from agent import Agent  # Import the Agent class
from ability import Ability  # Import the Ability class

# Create abilities
smoke_ability = Ability("Smokescreen", "Blocks vision for a short time", 30)
flash_ability = Ability("Flashbang", "Blinds enemies in a small radius", 45)

# Create an agent
phoenix = Agent("Phoenix", "Duelist")

# Add abilities to the agent
phoenix.add_ability(smoke_ability)
phoenix.add_ability(flash_ability)

# Print agent info and abilities
print(phoenix.agent_info())
phoenix.list_abilities()
