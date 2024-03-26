import pygame

pygame.init()
FPS = 60
W, H = 500, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('imag scal')
clock = pygame.time.Clock()


def load_image(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img


img = load_image('ing.png')
img1 = pygame.transform.scale(img, (200, 200))
img2 = pygame.transform.scale(img, (700, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        win.blit(img1, (0, 0))
    win.blit(img2, (100,200))
    pygame.display.update()
