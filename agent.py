# agent.py
from ability import Ability  # Import the Ability class

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def list_abilities(self):
        for ability in self.abilities:
            print(ability.ability_info())

    def agent_info(self):
        return f"Agent: {self.name}, Role: {self.role}"
