import pygame
from scripts.utils import load_images
from scripts.player import Player
from scripts.tilemap import Tilemap
from sys import exit


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Play')
        self.screen = pygame.display.set_mode((1000,500))
        self.display = pygame.Surface((500, 250))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 15)

        self.movement = [False, False]
        self.direction = 'right'
        
        self.assets = {
            'character/left': load_images('characters/girl sprites/left'),
            'character/right': load_images('characters/girl sprites/right'),
            'character/dying': load_images('characters/girl sprites/dying'),
            'tiles/grass': load_images('tiles/grass'),
            'tiles/stone': load_images('tiles/stone'),
        }

        self.player = Player(self, (50, 50), (24, 24))

        self.tilemap = Tilemap(self.display, self, 16)

    def render_text(self, screen, text, pos, color):
        text_surface = self.font.render(text, True, color)
        screen.blit(text_surface, pos)

    def run(self):
        while True:
            self.display.fill((0,0,0))

            self.tilemap.render()

            self.player.update(self.movement, self.tilemap, self.direction)
            self.player.render(self.display, self.direction)


            mouse_pos = pygame.mouse.get_pos()
            text = f"({mouse_pos[0]}, {mouse_pos[1]})"
            self.render_text(self.display, text, (self.display.get_width() - 50, 10), (255,255,255))


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
                        self.player.jump()
                    if event.key == pygame.K_LEFT:
                        pass
                    if event.key == pygame.K_RIGHT:
                        pass

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_SPACE:
                        pass
                    if event.key == pygame.K_LEFT:
                        pass
                    if event.key == pygame.K_RIGHT:
                        pass

        
        
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            # self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
