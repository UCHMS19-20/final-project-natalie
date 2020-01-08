import pygame
import sys
import random as randint
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

# "erases" title
pygame.time.delay(3000)
win.fill (black,(50,50,150,150))

# update display
pygame.display.flip()

# function for number of players
def player_num():
    # asks user for number of players
    num = int(input('''How many players are playing? 2 to 4 players
    '''))
    # validates user answer
    while num < 2 or num > 4:
        num = int(input('''You need 2 to 4 players to play this game. Try again
        '''))
    return num

# get number of players
player_num()

# display chips for 2 players
if num is 2:
    x = 0
    y = 0
    player_1 = pygame.draw.rect(win, blue, (x,y,5,5))
    x = 10
    y = 0
    player_2 = pygame.draw.rect(win, red, (x,y,5,5))
# display chips for 3 players
if num is 3:
    x = 0
    y = 0
    player_1 = pygame.draw.rect(win, blue, (x,y,5,5))
    x = 10
    y = 0
    player_2 = pygame.draw.rect(win, red, (x,y,5,5))
    x = 0
    y = 10
    player_3 = pygame.draw.rect(win, green, (x,y,5,5))
# display chips for 4 players
if num is 4:
    x = 0
    y = 0
    player_1 = pygame.draw.rect(win, blue, (x,y,5,5))
    x = 10
    y = 0
    player_2 = pygame.draw.rect(win, red, (x,y,5,5))
    x = 0
    y = 10
    player_3 = pygame.draw.rect(win, green, (x,y,5,5))
    x = 10
    y = 10
    player_4 = pygame.draw.rect(win, purple, (x,y,5,5))

# main loop
while True:
    # do something for each event in the event queue
    for event in pygame.event.get():
        # check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # exit the program
            sys.exit()
    keys = pygame.key.get_pressed
    print("It's player 1's turn. Press enter to roll the die")
    # random number between 1 and 6
    dice = randint(1,6)
    print(f'You rolled a {dice}')



    # update display
    pygame.display.flip()