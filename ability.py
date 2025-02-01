from ability import Ability  # Import the Ability class

class Ability:
    def __init__(self, name, description, cooldown) -> None:
        self.name = name
        self.description = description
        self.cooldown = cooldown
        
    def ability_info(self):
        return f"{self.name}: {self.description} (Cooldown: {self.cooldown}s)"