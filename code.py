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

# defined wait time
def wait(sec):
    pygame.time.delay(sec*1000)
    return

# defined board
def draw_board(self):
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

# defined title of game
def title(self):
    font = pygame.font.SysFont('Arial', 100)
    text = font.render('Gold', True, gold)
    win.blit(text, (130,120))
    text = font.render('Rush', True, gold)
    win.blit(text, (130,240))
    return

# player 1
p1 = {
    'x': 0,
    'y': 0,
    '$': 0
}

# player 2
p2 = {
    'x': 20,
    'y': 0,
    '$': 0
}

# player 3
p3 = {
    'x': 0,
    'y': 20,
    '$': 0
}

# player 4
p4 = {
    'x': 20,
    'y': 20,
    '$': 0
}

# function for number of players
def player_num(self):
    font = pygame.font.SysFont('Arial', 20)

    pygame.draw.rect(win, blue, (170,140,160,80))
    two_p = pygame.Rect(175,145,150,70)
    pygame.draw.rect(win, gold, two_p)
    text = font.render('2 players', True, black)
    win.blit(text, (210,170))

    pygame.draw.rect(win, blue, (70,260,160,80))
    three_p = pygame.Rect(75,265,150,70)
    pygame.draw.rect(win, gold, three_p)
    text = font.render('3 players', True, black)
    win.blit(text, (110,290))

    pygame.draw.rect(win, blue, (270,260,160,80))
    four_p = pygame.Rect(275,265,150,70)
    pygame.draw.rect(win, gold, four_p)
    text = font.render('4 players', True, black)
    win.blit(text, (310,290))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if two_p.collidepoint(pygame.mouse.get_pos()[0]):
            pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
            pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if three_p.collidepoint(pygame.mouse.get_pos()[0]):
            pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
            pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))
            pygame.draw.rect(win, green, (p3["x"],p3["y"],10,10))
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if four_p.collidepoint(pygame.mouse.get_pos()[0]):
            pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
            pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))
            pygame.draw.rect(win, green, (p3["x"],p3["y"],10,10))
            pygame.draw.rect(win, purple, (p4["x"],p4["y"],10,10))
    return

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.mouse.get_pressed():
            main = True


    intro = True
    while intro:
        # create window
        win = pygame.display.set_mode((500,500))
        win.fill (black)
        draw_board()
        title()
        # update display
        pygame.display.flip()
        # wait 3 seconds
        wait(3)
        # "erases" title
        win.fill (black,(100,100,300,300))
        # update display
        pygame.display.flip()
        # get number of players
        player_num()
    # wait 2 seconds
    wait(2)

    while main:
        print("It's player 1's turn")
        # wait 1 second
        wait(1)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p1['x'] += (dice*40)
        # update display
        pygame.display.flip()

        # wait 1 second
        wait(1)
        print("It's player 2's turn")
        # wait 1 second
        wait(1)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p2['x'] += (dice*40)
        # update display
        pygame.display.flip()

        if num is 3 or 4:
            # wait 1 second
            wait(1)
            print("It's player 3's turn")
            # wait 1 second
            wait(1)
            # random number between 1 and 6
            dice = random.randint(1,6)
            print(f'You rolled a {dice}')
            p3['x'] += (dice*40)
            # update display
            pygame.display.flip()

        if num is 4:
            # wait 1 second
            wait(1)
            print("It's player 4's turn")
            # wait 1 second
            wait(1)
            # random number between 1 and 6
            dice = random.randint(1,6)
            print(f'You rolled a {dice}')
            p4['x'] += (dice*40)
            # update display
            pygame.display.flip()
