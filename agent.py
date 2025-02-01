class Agent:
    def __init__(self, name, role, ability) -> None:
        self.name = name
        self.role = role
        self.ability =  []
        
    def add_ability(self,ability):
        self.ability.append[ability]
        
    def list_abilities(self):
        for ability in self.abilities:
            print(ability.ability_info())
            
    def agent_info(self):
        return f"Agent: {self.name}, Role: {self.role}"