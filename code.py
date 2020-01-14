import pygame
import sys
import random
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
win = pygame.display.set_mode((1000,1000))
win.fill (black)

# define width and height variables
width = 80
height = 80

# draw top row
x = -100
y = 0
for n in range(10):
    x += 100
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for top row
x = -200
y = 0
for n in range(2):
    x += 400
    pygame.draw.rect(win, gold, (x,y,width,height))

# draw bottom row
x = -100
y = 900
for n in range(10):
    x += 100
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for bottom row
x = -200
y = 900
for n in range(2):
    x += 500
    pygame.draw.rect(win, gold, (x,y,width,height))

# draw left column
x = 0
y = -100
for n in range(10):
    y += 100
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for left column
x = 0
y = -100
for n in range(3):
    y += 300
    pygame.draw.rect(win, gold, (x,y,width,height))

# draw right column
x = 900
y = -100
for n in range(10):
    y += 100
    pygame.draw.rect(win, white, (x,y,width,height))

# adds special spaces for right column
x = 900
y = -200
for n in range(3):
    y += 300
    pygame.draw.rect(win, gold, (x,y,width,height))

# print title of game
font = pygame.font.SysFont('Arial', 200)
text1 = font.render('Gold', True, gold)
text2 = font.render('Rush', True, gold)
win.blit(text1, (260,240))
win.blit(text2, (260,480))

# update display
pygame.display.flip()

# wait 3 seconds
pygame.time.delay(3000)
# "erases" title
win.fill (black,(200,200,600,600))

# update display
pygame.display.flip()

# player 1
p1 = {
    'x': 0,
    'y': 0
}

# player 2
p2 = {
    'x': 40,
    'y': 0
}

# player 3
p3 = {
    'x': 0,
    'y': 40
}

# player 4
p4 = {
    'x': 40,
    'y': 40
}

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
num = player_num()

# display chips for 2 players
if num is 2:
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],20,20))
    pygame.draw.rect(win, red, (p2["x"],p2["y"],20,20))
# display chips for 3 players
if num is 3:
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],20,20))
    pygame.draw.rect(win, red, (p2["x"],p2["y"],20,20))
    pygame.draw.rect(win, green, (p3["x"],p3["y"],20,20))
# display chips for 4 players
if num is 4:
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],20,20))
    pygame.draw.rect(win, red, (p2["x"],p2["y"],20,20))
    pygame.draw.rect(win, green, (p3["x"],p3["y"],20,20))
    pygame.draw.rect(win, purple, (p4["x"],p4["y"],20,20))

# update display
pygame.display.flip()

# wait 2 seconds
pygame.time.delay(2000)

# set number of rounds
rounds = 0

# set for 10 rounds
while rounds < 11:
    # add 1 to rounds every round
    rounds += 1

    print("It's player 1's turn")
    # wait 1 second
    pygame.time.delay(1000)
    # random number between 1 and 6
    dice1 = random.randint(1,6)
    print(f'You rolled a {dice}')
    p1['x'] += (dice*80)
    
    # wait 1 second
    pygame.time.delay(1000)

    print("It's player 2's turn")
    # wait 1 second
    pygame.time.delay(1000)
    # random number between 1 and 6
    dice = random.randint(1,6)
    print(f'You rolled a {dice}')
    p2['x'] += (dice*80)

    if num is 3 or 4:
        # wait 1 second
        pygame.time.delay(1000)
        print("It's player 3's turn")
        # wait 1 second
        pygame.time.delay(1000)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p3['x'] += (dice*80)

    if num is 4:
        # wait 1 second
        pygame.time.delay(1000)
        print("It's player 4's turn")
        # wait 1 second
        pygame.time.delay(1000)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p4['x'] += (dice*80)

    # update display
    pygame.display.flip()