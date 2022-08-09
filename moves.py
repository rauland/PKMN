class Move:
    def __init__(self, name, damage, type, accurary):
        self.name = name
        self.damage = damage
        self.type = type
        self.accurary = accurary

def get_move(move = "Tackle"):
    move_dict = {
    "Tackle":("Tackle",35,'Normal',100),
    "Thunderbolt":("Thunderbolt",50,'Electric',100),
    "Flamethrower":("Flamethrower",60,'Fire',100),
    "Water Gun":("Water Gun",40,'Water',100),
    "Vine Whip":("Vine Whip",45,'Grass',100),
    }
    return Move(*move_dict[move])