import pygame
import sys
# initiate pygame
pygame.init()

# get all fonts
all_fonts = pygame.font.get_fonts()

# colors
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)
gold = (212,175,55)

# create window
win = pygame.display.set_mode((250,250))
win.fill (black)

# define width and height variables
width = 20
height = 20

# draw top row
x = -25
y = 0
for n in range(10):
    x += 25
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for top row
x = -50
y = 0
for n in range(2):
    x += 100
    pygame.draw.rect(win, gold, (x,y,width,height))

# draw bottom row
x = -25
y = 225
for n in range(10):
    x += 25
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for bottom row
x = -50
y = 225
for n in range(2):
    x += 125
    pygame.draw.rect(win, gold, (x,y,width,height))

# draw left column
x = 0
y = -25
for n in range(10):
    y += 25
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for left column
x = 0
y = -25
for n in range(3):
    y += 75
    pygame.draw.rect(win, gold, (x,y,width,height))

# draw right column
x = 225
y = -25
for n in range(10):
    y += 25
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for right column
x = 225
y = -50
for n in range(3):
    y += 75
    pygame.draw.rect(win, gold, (x,y,width,height))

# print title of game
font = pygame.font.SysFont('Arial', 50)
text1 = font.render('Gold', True, gold)
text2 = font.render('Rush', True, gold)
win.blit(text1, (65,60))
win.blit(text2, (65,120))

# update display
pygame.display.flip()

# function for number of players
def player_num(num):
    if num is 2:
        x = 0
        y = 0
        chip = pygame.draw.rect(win, blue, (x,y,5,5))
        x = 10
        y = 0
        chip = pygame.draw.rect(win, red, (x,y,5,5))
    if num is 3:
        x = 0
        y = 0
        chip = pygame.draw.rect(win, blue, (x,y,5,5))
        x = 10
        y = 0
        chip = pygame.draw.rect(win, red, (x,y,5,5))
        x = 0
        y = 10
        chip = pygame.draw.rect(win, green, (x,y,5,5))
    if num is 4:
        x = 0
        y = 0
        chip = pygame.draw.rect(win, blue, (x,y,5,5))
        x = 10
        y = 0
        chip = pygame.draw.rect(win, red, (x,y,5,5))
        x = 0
        y = 10
        chip = pygame.draw.rect(win, green, (x,y,5,5))
        x = 10
        y = 10
        chip = pygame.draw.rect(win, purple, (x,y,5,5))
    return

# get number of players and display chips accordingly
player_num(input('''How many people are playing? 2 to 4 players
    '''))

# update display
pygame.display.flip()

# # main loop
# while True:
#     # do something for each event in the event queue (list of things that happen)
#     for event in pygame.event.get():
#         # Check to see if the current event is a QUIT event
#         if event.type == pygame.QUIT:
#             # If so, exit the program
#             sys.exit()
#         pygame.display.flip()