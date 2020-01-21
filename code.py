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

# state
state = 0

# creates window
win = pygame.display.set_mode((500,500))

# defined wait time
def wait(sec):
    pygame.time.delay(sec*1000)
    return

# defined board
def draw_board():
    global win
    s_width = 40
    s_height = 40
    # draw top row
    x = -50
    y = 0
    for n in range(10):
        x += 50
        pygame.draw.rect(win, white, (x,y,s_width,s_height))

    # adds special spaces for top row
    x = -100
    y = 0
    for n in range(2):
        x += 200
        special = pygame.Rect(x,y,s_width,s_height)
        pygame.draw.rect(win, gold, special)

    # draw bottom row
    x = -50
    y = 450
    for n in range(10):
        x += 50
        pygame.draw.rect(win, white, (x,y,s_width,s_height))

    # adds special spaces for bottom row
    x = -100
    y = 450
    for n in range(2):
        x += 250
        special = pygame.Rect(x,y,s_width,s_height)
        pygame.draw.rect(win, gold, special)

    # draw left column
    x = 0
    y = -50
    for n in range(10):
        y += 50
        pygame.draw.rect(win, white, (x,y,s_width,s_height))

    # adds special spaces for left column
    x = 0
    y = -50
    for n in range(3):
        y += 150
        special = pygame.Rect(x,y,s_width,s_height)
        pygame.draw.rect(win, gold, special)

    # draw right column
    x = 450
    y = -50
    for n in range(10):
        y += 50
        pygame.draw.rect(win, white, (x,y,s_width,s_height))

    # adds special spaces for right column
    x = 450
    y = -100
    for n in range(3):
        y += 150
        special = pygame.Rect(x,y,s_width,s_height)
        pygame.draw.rect(win, gold, special)
    return

# displays title of game
def title():
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
def player_num():
    font = pygame.font.SysFont('Arial', 20)
    p_width = 10
    p_height = 10
    # button for 2 players
    pygame.draw.rect(win, blue, (170,140,160,80))
    two_p = pygame.Rect(175,145,150,70)
    pygame.draw.rect(win, gold, two_p)
    text = font.render('2 players', True, black)
    win.blit(text, (210,170))
    
    # button for 3 players
    pygame.draw.rect(win, blue, (70,260,160,80))
    three_p = pygame.Rect(75,265,150,70)
    pygame.draw.rect(win, gold, three_p)
    text = font.render('3 players', True, black)
    win.blit(text, (110,290))
    
    # button for 4 players
    pygame.draw.rect(win, blue, (270,260,160,80))
    four_p = pygame.Rect(275,265,150,70)
    pygame.draw.rect(win, gold, four_p)
    text = font.render('4 players', True, black)
    win.blit(text, (310,290))
    

    # if 2 player button is pressed, 2 chips will be displayed
    if event.type == pygame.MOUSEBUTTONDOWN:
        if two_p.collidepoint(pygame.mouse.get_pos()[0]):
            player1 = pygame.Rect(p1["x"],p1["y"],p_width,p_height)
            pygame.draw.rect(win, blue, player1)
            player2 = pygame.Rect(p2["x"],p2["y"],p_width,p_height)
            pygame.draw.rect(win, red, player2)
            num = 2
    
    # if 3 player button is pressed, 3 chips will be displayed
    if event.type == pygame.MOUSEBUTTONDOWN:
        if three_p.collidepoint(pygame.mouse.get_pos()[0]):
            player1 = pygame.Rect(p1["x"],p1["y"],p_width,p_height)
            pygame.draw.rect(win, blue, player1)
            player2 = pygame.Rect(p2["x"],p2["y"],p_width,p_height)
            pygame.draw.rect(win, red, player2)
            player3 = pygame.Rect(p3["x"],p3["y"],p_width,p_height)
            pygame.draw.rect(win, green, player3)
            num = 3
    
    # if 4 player button is pressed, 4 chips will be displayed
    if event.type == pygame.MOUSEBUTTONDOWN:
        if four_p.collidepoint(pygame.mouse.get_pos()[0]):
            player1 = pygame.Rect(p1["x"],p1["y"],p_width,p_height)
            pygame.draw.rect(win, blue, player1)
            player2 = pygame.Rect(p2["x"],p2["y"],p_width,p_height)
            pygame.draw.rect(win, red, player2)
            player3 = pygame.Rect(p3["x"],p3["y"],p_width,p_height)
            pygame.draw.rect(win, green, player3)
            player4 = pygame.Rect(p4["x"],p4["y"],p_width,p_height)
            pygame.draw.rect(win, purple, player4)
            num = 4
    return num

# stage 0 is the intro stage
def stage_0():
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            state += 1
    # makes window black
    win.fill (black)
    # draws game board
    draw_board()
    # displays title of game
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
    num = player_num()

def stage_1():
    # wait 2 seconds
    wait(2)
    print("It's Player 1's turn")
    # wait 1 second
    wait(1)
    # random number between 1 and 6
    dice = random.randint(1,6)
    print(f'You rolled a {dice}')
    move = dice*40
    p1['x'] += move
    if p1['x'] >= 500:
        p1['x'] -= 500
        p1['y'] += p1['x']
        p1['x'] = 460
    pygame.draw.rect(win, blue, (p1["x"],p1["y"],10,10))
    if player1.colliderect(special):
        p1['$'] += 100
        print(f"Player 1 now has ${p1['$']}")
    # update display
    pygame.display.flip()

    # wait 1 second
    wait(1)
    print("It's Player 2's turn")
    # wait 1 second
    wait(1)
    # random number between 1 and 6
    dice = random.randint(1,6)
    print(f'You rolled a {dice}')
    p2['x'] += (dice*40)
    pygame.draw.rect(win, red, (p2["x"],p2["y"],10,10))
    # update display
    pygame.display.flip()

    if num is 3 or 4:
        # wait 1 second
        wait(1)
        print("It's Player 3's turn")
        # wait 1 second
        wait(1)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p3['x'] += (dice*40)
        pygame.draw.rect(win, green, (p3["x"],p3["y"],10,10))
        # update display
        pygame.display.flip()

    if num is 4:
        # wait 1 second
        wait(1)
        print("It's Player 4's turn")
        # wait 1 second
        wait(1)
        # random number between 1 and 6
        dice = random.randint(1,6)
        print(f'You rolled a {dice}')
        p4['x'] += (dice*40)
        pygame.draw.rect(win, purple, (p4["x"],p4["y"],10,10))
        # update display
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

while True:
    if state == 0:
        stage_0()
    else:
        stage_1()
