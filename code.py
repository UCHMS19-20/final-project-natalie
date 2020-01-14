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
win = pygame.display.set_mode((500,500))
win.fill (black)

def draw_board():
    width = 40
    height = 40
    # draw top row
    x = -50
    y = 0
    for n in range(10):
        x += 50
        pygame.draw.rect(win, white, (x,y,width,height))

    # adds special spaces for top row
    x = -100
    y = 0
    for n in range(2):
        x += 200
        pygame.draw.rect(win, gold, (x,y,width,height))

    # draw bottom row
    x = -50
    y = 450
    for n in range(10):
        x += 50
        pygame.draw.rect(win, white, (x,y,width,height))

    # adds special spaces for bottom row
    x = -100
    y = 450
    for n in range(2):
        x += 250
        pygame.draw.rect(win, gold, (x,y,width,height))

    # draw left column
    x = 0
    y = -50
    for n in range(10):
        y += 50
        pygame.draw.rect(win, white, (x,y,width,height))

    # adds special spaces for left column
    x = 0
    y = -50
    for n in range(3):
        y += 150
        pygame.draw.rect(win, gold, (x,y,width,height))

    # draw right column
    x = 450
    y = -50
    for n in range(10):
        y += 50
        pygame.draw.rect(win, white, (x,y,width,height))

    # adds special spaces for right column
    x = 450
    y = -100
    for n in range(3):
        y += 150
        pygame.draw.rect(win, gold, (x,y,width,height))
    return

draw_board()

# print title of game
font = pygame.font.SysFont('Arial', 100)
text1 = font.render('Gold', True, gold)
text2 = font.render('Rush', True, gold)
win.blit(text1, (130,120))
win.blit(text2, (130,240))

# update display
pygame.display.flip()

# wait 3 seconds
pygame.time.delay(3000)
# "erases" title
win.fill (black,(100,100,300,300))

# update display
pygame.display.flip()

# player 1
p1 = {
    'x': 0,
    'y': 0
}

# player 2
p2 = {
    'x': 20,
    'y': 0
}

# player 3
p3 = {
    'x': 0,
    'y': 20
}

# player 4
p4 = {
    'x': 20,
    'y': 20
}

# function for number of players
def player_num():
    pygame.draw.rect(win, gold, (x,y,width,height))
    return num

# get number of players
num = player_num()

# display chips for 2 players
if num is 2:
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
    pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))
# display chips for 3 players
if num is 3:
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
    pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))
    pygame.draw.rect(win, green, (p3["x"],p3["y"],10,10))
# display chips for 4 players
if num is 4:
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
    pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))
    pygame.draw.rect(win, green, (p3["x"],p3["y"],10,10))
    pygame.draw.rect(win, purple, (p4["x"],p4["y"],10,10))

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
    p1['x'] += (dice*40)
    
    # wait 1 second
    pygame.time.delay(1000)

    print("It's player 2's turn")
    # wait 1 second
    pygame.time.delay(1000)
    # random number between 1 and 6
    dice = random.randint(1,6)
    print(f'You rolled a {dice}')
    p2['x'] += (dice*40)

    if num is 3 or 4:
        # wait 1 second
        pygame.time.delay(1000)
        print("It's player 3's turn")
        # wait 1 second
        pygame.time.delay(1000)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p3['x'] += (dice*40)

    if num is 4:
        # wait 1 second
        pygame.time.delay(1000)
        print("It's player 4's turn")
        # wait 1 second
        pygame.time.delay(1000)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p4['x'] += (dice*40)

    # update display
    pygame.display.flip()