class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(f'{self.name} constructed')

    def party(self):
        self.x = self.x + 1
        print(f'{self.name} party count {self.x}')


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(f'{self.name} points {self.points}')


robin = FootballFan('Robin')
robin.party()
robin.touchdown()
