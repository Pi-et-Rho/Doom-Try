class Player:
    def __init__(self, nom, pos_X, pos_Y, speed):
        self.nom = nom
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.speed = speed

    def Player(self, player_X, player_Y):
        self.pos_X += player_X * self.speed
        self.pos_Y += player_Y * self.speed