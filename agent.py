class Agent:
    def __init__(self, name, role, health=100):
        self.name = name
        self.role = role
        self.health = health
        self.level = 1
        self.abilities = []

    def add_ability(self, ability):
        """Adds an ability to the agent."""
        if isinstance(ability, Ability):
            self.abilities.append(ability)
        else:
            print("Invalid ability.")

    def use_ability(self, ability_name):
        """Uses the specified ability."""
        for ability in self.abilities:
            if ability.name == ability_name:
                ability.use()
                return
        print(f"Ability {ability_name} not found for {self.name}.")

    def level_up(self):
        """Levels up the agent, improving health and abilities."""
        self.level += 1
        self.health += 20  # Increase health by 20 for each level
        print(f"{self.name} leveled up to Level {self.level}! Health increased to {self.health}.")

    def reduce_ability_cooldowns(self, time_passed):
        """Reduces cooldown of all abilities."""
        for ability in self.abilities:
            ability.reduce_cooldown(time_passed)

    def agent_info(self):
        """Returns basic information about the agent."""
        return f"Agent: {self.name}, Role: {self.role}, Health: {self.health}, Level: {self.level}"

    def list_abilities(self):
        """Lists all abilities of the agent."""
        if self.abilities:
            for ability in self.abilities:
                print(ability)
        else:
            print(f"{self.name} has no abilities.")
