import pygame.sprite


class Stones(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))


if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
    self.game_over += 1
if self.game_over == 5:
    self.player.update(0, 0)
    self.end_screen()
    run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        Stone(event.pos)

self.player.update(0, 0)
                    self.player, self.level_x, self.level_y = self.generate_level(self.load_level('level_1.txt'))


if self.rect.right > WIDTH:
        self.rect.right = WIDTH
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.bottom > HEIGHT:
        self.rect.bottom = HEIGHT
    if self.rect.top < 0:
        self.rect.top = 0