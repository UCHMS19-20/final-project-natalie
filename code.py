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


blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)

# chip_color = input('''Choose your color: blue, red, green, yellow
# ''')

# if chip_color is blue:
x = 0
y = 0
chip = pygame.draw.rect(win, blue, (x,y,5,5))

# if chip_color is red:
x = 10
y = 0
chip = pygame.draw.rect(win, red, (x,y,5,5))

# if chip_color is green:
x = 0
y = 10
chip = pygame.draw.rect(win, green, (x,y,5,5))

# if chip_color is purple:
x = 10
y = 10
chip = pygame.draw.rect(win, purple, (x,y,5,5))

pygame.display.flip()