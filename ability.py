class Ability:
    def __init__(self, name, effect, cooldown):
        self.name = name
        self.effect = effect
        self.cooldown = cooldown  # Cooldown in seconds
        self.current_cooldown = 0  # Starts with no cooldown

    def use(self):
        """Uses the ability and starts the cooldown."""
        if self.is_usable():
            print(f"Using ability: {self.name} - {self.effect}")
            self.current_cooldown = self.cooldown
        else:
            print(f"Ability {self.name} is on cooldown for {self.current_cooldown} more seconds.")

    def reduce_cooldown(self, time_passed):
        """Reduces cooldown based on time passed."""
        if self.current_cooldown > 0:
            self.current_cooldown = max(0, self.current_cooldown - time_passed)
    
    def is_usable(self):
        """Checks if the ability is ready to use."""
        return self.current_cooldown == 0

    def __str__(self):
        return f"{self.name}: {self.effect} (Cooldown: {self.cooldown}s)"
