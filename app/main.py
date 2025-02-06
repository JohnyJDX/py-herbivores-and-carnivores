class Animal:
    alive = []
    def __init__(self, name: str, health=100, hidden = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self):
        if self.health <= 0:
            print(f"{self.name} is dead.")
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden



class Carnivore(Animal):
    def bite(self, herbivore: list):
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden:
                print(f"{herbivore.name} is hidden, cannot bite.")
            else:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    herbivore.die()
        else:
            print(f"{self.name} cannot bite another carnivore.")
