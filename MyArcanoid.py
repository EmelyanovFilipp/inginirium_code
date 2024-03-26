import pygame

from spryts.block import Block
from spryts.plain import Plain
from spryts.ball import Ball

pygame.init()
win = pygame.display.set_mode((740, 800))
pygame.display.set_caption('MyArcanoid')
pygame.display.set_icon(pygame.image.load('ing.png'))

score = 0
pygame.font.init()
my_font = pygame.font.SysFont('cocmic sans ms',30)
score += 141


surf_font = my_font.render(f'score:',False,(255,)*3)
win.blit(surf_font,(20,0))

all_sprites = pygame.sprite.Group()
plain = Plain(690, all_sprites)
ball = Ball(all_sprites)

blocks = pygame.sprite.Group()
for i in range(28):
    for j in range(3):
        Block(20 + 23 * i, 200 + 20 * j, 1, '#D0A94C', blocks, all_sprites)
    for j in range(3):
        Block(20 + 25 * i, 100 + 20 * j, 3, (240, 100, 20), blocks, all_sprites)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if ball.rect.colliderect(plain.rect):
        ball.collision(plain.rect.center)

    collision_blocks = pygame.sprite.spritecollide(ball,blocks,True)
    if collision_blocks is not None :
        if len(collision_blocks) > 0:
            ball.block_collision(collision_blocks[0].rect.center)

    all_sprites.update()
    win.fill((0,) * 3)
    all_sprites.draw(win)
    pygame.display.update()
    clock.tick(110)
    win.blit(surf_font,(0,0))