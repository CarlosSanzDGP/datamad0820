
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.name = name

    def receiveDamage(self, damage):
        super().receiveDamage(damage) 
        if self.health < 1:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"  

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    
    def receiveDamage(self, damage):
  
        super().receiveDamage(damage) 
        if self.health < 1:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"        
    

# War


class War:
    pass
