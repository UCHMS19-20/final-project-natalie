import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)

win = pygame.display.set_mode((250,250))
win.fill (black)

width = 20
height = 20
margin = 5

x = -25
y = 0
for n in range(10):
    x += 25
    pygame.draw.rect(win, white, (x,y,width,height))

x = -25
y = 225
for n in range(10):
    x += 25
    pygame.draw.rect(win, white, (x,y,width,height))

x = 0
y = -25
for n in range(10):
    y += 25
    pygame.draw.rect(win, white, (x,y,width,height))

x = 225
y = -25
for n in range(10):
    y += 25
    pygame.draw.rect(win, white, (x,y,width,height))

pygame.display.flip()
