from agent import Agent
from ability import Ability

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

# Use abilities and level up
phoenix.use_ability("Smokescreen")
phoenix.level_up()

# Reduce cooldowns by 10 seconds
phoenix.reduce_ability_cooldowns(10)
phoenix.use_ability("Smokescreen")
