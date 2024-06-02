import pygame

class Player():
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        self.count = 0
        self.action = "right"
        self.speed = 1

    def update(self, movement):
        self.movement = list(movement)

        if self.movement[0]:
            self.pos[0] -= self.speed
        if self.movement[1]:
            self.pos[0] += self.speed

    def animation(self, direction):
        if self.action != direction:
            self.action = direction
            self.count = 0
            
        lim = 0
        for img in self.game.assets['character/' + self.action]:
            lim += 1

        self.count += 0.1
        if self.count > lim - 1:
            self.count = 0

        return self.game.assets['character/' + self.action][int(self.count)]

    def render(self, surf, direction):
        surf.blit(self.animation(direction), self.pos)

        











