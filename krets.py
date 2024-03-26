import pygame

w,h = [int(t)for t in input().split()]
win = pygame.display.set_mode((w,h))

win.fill((255,255,255))

pygame.draw.line(win,(0,0,0),[0,0 ],[ w,h])
pygame.draw.line(win,(0,0,0),[0,h ], [w,0 ])

pygame.display.update()
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           exit()




















