import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
win.fill((255, 255, 255))

x = 250
y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



win = pygame.display.set_mode((500, 500))

    else:
        if x > 250:
            x -= 3
        elif x < 250:
            x += 3
        if y > 250:
         y -= 3
        elif y < 250:
            y += 3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -=3
    elif keys[pygame.K_d]:
        x +=3
    elif keys[pygame.K_w]:
        y -=3
    elif keys[pygame.K_s]:
        y +=3



win.fill((255, 255, 255))
pygame.draw.circle(win, (0, 0, 0), (x, y), 50)
pygame.display.update()
pygame.time.delay(10)
