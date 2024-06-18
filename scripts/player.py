import pygame

class Player():
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = list(size)
        self.count = 0
        self.action = "right"
        self.speed = 1
        self.airTime = 0
        self.acelleration = 1

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, movement, tilemap, direction):
        self.movement = list(movement)
        self.XmoveToDo = self.speed

        if self.movement[0]:
            player_rect = self.rect()
            pos = [player_rect.x - (2 * self.XmoveToDo), player_rect.y]
            for tile in tilemap.tiles_around(pos):
                if player_rect.colliderect(tile):
                    self.XmoveToDo = 0
            self.pos[0] -= self.XmoveToDo

        if self.movement[1]:
            player_rect = self.rect()
            pos = [player_rect.x + (2 * self.XmoveToDo), player_rect.y]
            for tile in tilemap.tiles_around(pos):
                if player_rect.colliderect(tile):
                    self.XmoveToDo = 0
            self.pos[0] += self.XmoveToDo

        
        
        player_rect = self.rect()
        self.YmoveToDo = self.speed + self.acelleration
        pos = [player_rect.x, player_rect.y + (self.YmoveToDo * 2)]
        for tile in tilemap.tiles_around(pos):
            if player_rect.colliderect(tile):
                print("Collide")
                self.acelleration = 0
                self.YmoveToDo = 0
            else:
                self.acelleration += 1        

        self.pos[1] += self.YmoveToDo

    def jump(self):
        pass

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
        # self.pos[0] = self.pos[0] - (self.game.display.get_width() / 2)
        # self.pos[1] = self.pos[1] - (self.game.display.get_height() / 2)

        surf.blit(self.animation(direction), self.pos)

        











