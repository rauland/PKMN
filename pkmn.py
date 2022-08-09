from role import Role
from moves import get_move

class Pokemon:
    def __init__(self, name, type, health, move = []):
        Role.__init__(self, name, type)
        self.health = health
        self.__max_health = health
        if move == []:
            self.move = []
            self.move += [get_move()]

    def attack(self, opponent, move = 0):
        opponent.health -= self.move[move].damage
        print(f"{self.name} used {self.move[move].name}! It did {self.move[move].damage} damage to {opponent.name}")

    def status(self):
        print(f'{self.name} current health is: {self.health}')
        
    def moveset(self):
        i = 0
        while i < len(self.move):
            print(f'{self.name} knows the move {self.move[i].name} which is a {self.move[i].type} type move.'); i+=1
        
    def potion(self):
        self.health = self.__max_health
        print(f'{self.name} health restored to max: {self.health}')

    def learn_move(self, move):
        self.move += [get_move(move)]