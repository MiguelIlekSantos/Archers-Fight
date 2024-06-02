import pygame
from scripts.utils import load_images
from scripts.player import Player
from sys import exit


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Play')
        self.screen = pygame.display.set_mode((1000,500))
        self.display = pygame.Surface((500, 250))
        self.clock = pygame.time.Clock()

        #                Left | Right | Jump | ShotLeft | ShotRight
        self.movement = [False, False, False, False, False]
        self.direction = 'right'
        
        self.assets = {
            'character/left': load_images('characters/girl sprites/left'),
            'character/right': load_images('characters/girl sprites/right'),
            'character/dying': load_images('characters/girl sprites/dying'),
        }

        self.player = Player(self, (0, 0))

    def run(self):
        while True:
            self.display.fill((0,0,0))

            self.player.update(self.movement)
            self.player.render(self.display, self.direction)











            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                        self.direction = 'left'
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                        self.direction = 'right'
                    if event.key == pygame.K_SPACE:
                        self.movement[2] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[3] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[4] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_SPACE:
                        self.movement[2] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[3] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[4] = False

        
        
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
