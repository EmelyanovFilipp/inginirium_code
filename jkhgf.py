import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
win.fill((255, 255, 255))

x = 100
y = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    y = y + 1
    x += 1
    if y > 500:
        y = 0
    if x >500:
        x = 0
    win.fill((255, 255, 255))
    pygame.draw.circle(win, (0, 0, 255), (250, y), 50)
    pygame.draw.rect(win, (255, 0, 0), (x, 250, 250, 100))
    pygame.display.update()
    pygame.time.delay(10)



















    # x = 50
    # y = 100
    #
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             exit()
    # x = x + 1
    #
    # win.fill((255, 255, 255))
    # pygame.draw.circle(win, (0, 0, 255), (y, x), 50)
    # pygame.draw.rect(win, (255, 0, 0), (y, x,100 , 250))
    # pygame.display.update()
    # pygame.time.delay(10)