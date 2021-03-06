import pygame
import sys
import random
# initiate pygame
pygame.init()

# get all fonts
all_fonts = pygame.font.get_fonts()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
gold = (212, 175, 55)

# base variables
state = 0
special = 0
num = 0
click = False
direction_1 = 1
direction_2 = 1
direction_3 = 1
direction_4 = 1

# creates window
win = pygame.display.set_mode((500, 500))


# defined wait time
def wait(sec):
    pygame.time.wait(sec*1000)
    return


# defined board
def draw_board():
    global win
    global special
    s_width = 40
    s_height = 40
    # draw top row
    x = -50
    y = 0
    for n in range(10):
        x += 50
        pygame.draw.rect(win, white, (x, y, s_width, s_height))

    # adds special spaces for top row
    x = -100
    y = 0
    for n in range(2):
        x += 200
        special = pygame.Rect(x, y, s_width, s_height)
        pygame.draw.rect(win, gold, special)

    # draw bottom row
    x = -50
    y = 450
    for n in range(10):
        x += 50
        pygame.draw.rect(win, white, (x, y, s_width, s_height))

    # adds special spaces for bottom row
    x = -100
    y = 450
    for n in range(2):
        x += 250
        special = pygame.Rect(x, y, s_width, s_height)
        pygame.draw.rect(win, gold, special)

    # draw left column
    x = 0
    y = -50
    for n in range(10):
        y += 50
        pygame.draw.rect(win, white, (x, y, s_width, s_height))

    # adds special spaces for left column
    x = 0
    y = -50
    for n in range(3):
        y += 150
        special = pygame.Rect(x, y, s_width, s_height)
        pygame.draw.rect(win, gold, special)

    # draw right column
    x = 450
    y = -50
    for n in range(10):
        y += 50
        pygame.draw.rect(win, white, (x, y, s_width, s_height))

    # adds special spaces for right column
    x = 450
    y = -100
    for n in range(3):
        y += 150
        special = pygame.Rect(x, y, s_width, s_height)
        pygame.draw.rect(win, gold, special)
    return


# displays title of game
def title():
    font = pygame.font.SysFont('Arial', 100)
    text = font.render('Gold', True, gold)
    win.blit(text, (130, 120))
    text = font.render('Rush', True, gold)
    win.blit(text, (130, 240))
    return


# player 1
p1 = {'x': 0, 'y': 0, '$': 0}
# player 2
p2 = {'x': 20, 'y': 0, '$': 0}
# player 3
p3 = {'x': 0, 'y': 20, '$': 0}
# player 4
p4 = {'x': 20, 'y': 20, '$': 0}

p_width = 10
p_height = 10
player1 = pygame.Rect(p1["x"], p1["y"], p_width, p_height)
player2 = pygame.Rect(p2["x"], p2["y"], p_width, p_height)
player3 = pygame.Rect(p3["x"], p3["y"], p_width, p_height)
player4 = pygame.Rect(p4["x"], p4["y"], p_width, p_height)


# function for number of players
def player_num():
    global player1
    global player2
    global player3
    global player4
    global state
    global num

    font = pygame.font.SysFont('Arial', 20)
    # button for 2 players
    pygame.draw.rect(win, blue, (170, 140, 160, 80))
    two_p = pygame.Rect(175, 145, 150, 70)
    pygame.draw.rect(win, gold, two_p)
    text = font.render('2 players', True, black)
    win.blit(text, (210, 170))

    # button for 3 players
    pygame.draw.rect(win, blue, (70, 260, 160, 80))
    three_p = pygame.Rect(75, 265, 150, 70)
    pygame.draw.rect(win, gold, three_p)
    text = font.render('3 players', True, black)
    win.blit(text, (110, 290))

    # button for 4 players
    pygame.draw.rect(win, blue, (270, 260, 160, 80))
    four_p = pygame.Rect(275, 265, 150, 70)
    pygame.draw.rect(win, gold, four_p)
    text = font.render('4 players', True, black)
    win.blit(text, (310, 290))

    # update display
    pygame.display.flip()

    if event.type == pygame.MOUSEBUTTONDOWN:
        # if 2 player button is pressed, 2 chips will be displayed
        if two_p.collidepoint(pygame.mouse.get_pos()):
            num = 2
            pygame.draw.rect(win, blue, player1)
            pygame.draw.rect(win, red, player2)
            state += 1
            # erases player buttons
            win.fill(black, (50, 50, 400, 400))
            # update display
            pygame.display.flip()

        # if 3 player button is pressed, 3 chips will be displayed
        if three_p.collidepoint(pygame.mouse.get_pos()):
            num = 3
            pygame.draw.rect(win, blue, player1)
            pygame.draw.rect(win, red, player2)
            pygame.draw.rect(win, green, player3)
            state += 1
            # erases player buttons
            win.fill(black, (50, 50, 400, 400))
            # update display
            pygame.display.flip()

        # if 4 player button is pressed, 4 chips will be displayed
        if four_p.collidepoint(pygame.mouse.get_pos()):
            num = 4
            pygame.draw.rect(win, blue, player1)
            pygame.draw.rect(win, red, player2)
            pygame.draw.rect(win, green, player3)
            pygame.draw.rect(win, purple, player4)
            state += 1
            # erases player buttons
            win.fill(black, (50, 50, 400, 400))
            # update display
            pygame.display.flip()
    return


# stage 0 is the intro stage
def stage_0():
    # "erases" title
    win.fill(black, (100, 100, 300, 300))
    # get number of players
    player_num()
    return


# stage 1 is game stage
def stage_1():
    global player1
    global player2
    global player3
    global player4
    global direction_1
    global direction_2
    global direction_3
    global direction_4
    global num
    wait(3)
    font = pygame.font.SysFont('Arial', 20)

    # player 1's turn
    # clears middle of window
    win.fill(black, (50, 50, 400, 400))
    pygame.display.flip()
    # indicates player 1's turn
    text = font.render("It's Player 1's turn", True, white)
    win.blit(text, (130, 120))
    pygame.display.flip()
    wait(5)
    # clears middle of window
    win.fill(black, (50, 50, 400, 400))
    pygame.display.flip()
    # random number between 1 and 6
    dice = random.randint(1, 6)
    # display dice roll
    text = font.render('You rolled a', True, white)
    win.blit(text, (130, 120))
    text = font.render(str(dice), True, white)
    win.blit(text, (130, 150))
    pygame.display.flip()
    wait(3)
    move = dice*50

    # if out of bounds, player chip changes direction
    if p1['x'] >= 450:
        p1['x'] -= 500
        p1['y'] += p1['x']
        p1['x'] = 460
        direction_1 = 1
    if p1['y'] >= 450:
        p1['y'] -= 500
        p1['x'] -= p1['y']
        p1['y'] = 460
        direction_1 = 2
    if p1['x'] < 0:
        p1['y'] -= p1['x']
        p1['x'] = 0
        direction_1 = 3
    if p1['y'] < 0:
        p1['x'] -= p1['y']
        p1['y'] = 0
        direction_1 = 4

    # player 1's chip moves
    if direction_1 == 1:
        p1['x'] += move
    if direction_1 == 2:
        p1['y'] += move
    if direction_1 == 3:
        p1['x'] -= move
    if direction_1 == 4:
        p1['y'] -= move

    # update the board with new player position
    draw_board()
    pygame.draw.rect(win, blue, (p1["x"], p1["y"], 10, 10))
    pygame.draw.rect(win, red, (p2["x"], p2["y"], 10, 10))
    if num == 3 or num == 4:
        pygame.draw.rect(win, green, (p3["x"], p3["y"], 10, 10))
    if num == 4:
        pygame.draw.rect(win, purple, (p4["x"], p4["y"], 10, 10))
    pygame.display.flip()
    
    # clears middle of window
    win.fill(black, (50, 50, 400, 400))
    pygame.display.flip()
    
    # if player lands on special space, they receive $100
    if player1.colliderect(special):
        p1['$'] += 100
        text = font.render('Player 1 now has', True, white)
        win.blit(text, (130, 120))
        text = font.render(str(p1['$']), True, white)
        win.blit(text, (130, 150))
        pygame.display.flip()
    wait(4)
    
    # player 2's turn
    # clears middle of window
    win.fill(black, (50, 50, 400, 400))
    pygame.display.flip()
    # indicates player 2's turn
    text = font.render("It's Player 2's turn", True, white)
    win.blit(text, (130, 120))
    pygame.display.flip()
    wait(5)
    # clears middle of window
    win.fill(black, (50, 50, 400, 400))
    pygame.display.flip()
    # random number between 1 and 6
    dice = random.randint(1, 6)
    # display dice roll
    text = font.render('You rolled a', True, white)
    win.blit(text, (130, 120))
    text = font.render(str(dice), True, white)
    win.blit(text, (130, 150))
    pygame.display.flip()
    wait(3)
    move = dice*50

    # if out of bounds, player chip changes direction
    if p2['x'] >= 450:
        p2['x'] -= 500
        p2['y'] += p2['x']
        p2['x'] = 460
        direction_2 = 1
    if p2['y'] >= 450:
        p2['y'] -= 500
        p2['x'] -= p2['y']
        p2['y'] = 460
        direction_2 = 2
    if p2['x'] < 0:
        p2['y'] -= p2['x']
        p2['x'] = 0
        direction_2 = 3
    if p2['y'] < 0:
        p2['x'] -= p2['y']
        p2['y'] = 0
        direction_2 = 4

    # player 2's chip moves
    if direction_2 == 1:
        p2['x'] += move
    if direction_2 == 2:
        p2['y'] += move
    if direction_2 == 3:
        p2['x'] -= move
    if direction_2 == 4:
        p2['y'] -= move

    # update the board with new player position
    draw_board()
    pygame.draw.rect(win, blue, (p1["x"], p1["y"], 10, 10))
    pygame.draw.rect(win, red, (p2["x"], p2["y"], 10, 10))
    if num == 3 or num == 4:
        pygame.draw.rect(win, green, (p3["x"], p3["y"], 10, 10))
    if num == 4:
        pygame.draw.rect(win, purple, (p4["x"], p4["y"], 10, 10))
    pygame.display.flip()

    # clears middle of window
    win.fill(black, (50, 50, 400, 400))
    pygame.display.flip()
    
    # if player lands on special space, they receive $100
    if player2.colliderect(special):
        p2['$'] += 100
        text = font.render('Player 2 now has', True, white)
        win.blit(text, (130, 120))
        text = font.render(str(p2['$']), True, white)
        win.blit(text, (130, 150))
        pygame.display.flip()
    wait(4)

    if num == 3 or num == 4:
        # player 3's turn
        # clears middle of window
        win.fill(black, (50, 50, 400, 400))
        pygame.display.flip()
        # indicates player 3's turn
        text = font.render("It's Player 3's turn", True, white)
        win.blit(text, (130, 120))
        pygame.display.flip()
        wait(5)
        # clears middle of window
        win.fill(black, (50, 50, 400, 400))
        pygame.display.flip()
        # random number between 1 and 6
        dice = random.randint(1, 6)
        # display dice roll
        text = font.render('You rolled a', True, white)
        win.blit(text, (130, 120))
        text = font.render(str(dice), True, white)
        win.blit(text, (130, 150))
        pygame.display.flip()
        wait(3)
        move = dice*50

        # if out of bounds, player chip changes direction
        if p3['x'] >= 500:
            p3['x'] -= 500
            p3['y'] += p3['x']
            p3['x'] = 460
            direction_3 = 1
        if p3['y'] >= 500:
            p3['y'] -= 500
            p3['x'] -= p3['y']
            p3['y'] = 460
            direction_3 = 2
        if p3['x'] < 0:
            p3['y'] -= p3['x']
            p3['x'] = 0
            direction_3 = 3
        if p3['y'] < 0:
            p3['x'] -= p3['y']
            p3['y'] = 0
            direction_3 = 4

        # player 3's chip moves
        if direction_3 == 1:
            p3['x'] += move
        if direction_3 == 2:
            p3['y'] += move
        if direction_3 == 3:
            p3['x'] -= move
        if direction_3 == 4:
            p3['y'] -= move

        # update the board with new player position
        draw_board()
        pygame.draw.rect(win, blue, (p1["x"], p1["y"], 10, 10))
        pygame.draw.rect(win, red, (p2["x"], p2["y"], 10, 10))
        pygame.draw.rect(win, green, (p3["x"], p3["y"], 10, 10))
        if num == 4:
            pygame.draw.rect(win, purple, (p4["x"], p4["y"], 10, 10))
        pygame.display.flip()

        # clears middle of window
        win.fill(black, (50, 50, 400, 400))
        pygame.display.flip()
        
        # if player lands on special space, they receive $100
        if player3.colliderect(special):
            p3['$'] += 100
            text = font.render('Player 3 now has', True, white)
            win.blit(text, (130, 120))
            text = font.render(str(p3['$']), True, white)
            win.blit(text, (130, 150))
            pygame.display.flip()
        wait(4)

    if num == 4:
        # player 4's turn
        # clears middle of window
        win.fill(black, (50, 50, 400, 400))
        pygame.display.flip()
        text = font.render("It's Player 4's turn", True, white)
        win.blit(text, (130, 120))
        pygame.display.flip()
        wait(5)
        # clears middle of window
        win.fill(black, (50, 50, 400, 400))
        pygame.display.flip()
        # random number between 1 and 6
        dice = random.randint(1, 6)
        # display dice roll
        text = font.render('You rolled a', True, white)
        win.blit(text, (130, 120))
        text = font.render(str(dice), True, white)
        win.blit(text, (130, 150))
        pygame.display.flip()
        wait(3)
        move = dice*50

        # if out of bounds, player chip changes direction
        if p4['x'] >= 500:
            p4['x'] -= 500
            p4['y'] += p4['x']
            p4['x'] = 460
            direction_4 = 1
        if p4['y'] >= 500:
            p4['y'] -= 500
            p4['x'] -= p4['y']
            p4['y'] = 460
            direction_4 = 2
        if p4['x'] < 0:
            p4['y'] -= p4['x']
            p4['x'] = 0
            direction_4 = 3
        if p4['y'] < 0:
            p4['x'] -= p4['y']
            p4['y'] = 0
            direction_4 = 4

        # player 1's chip moves
        if direction_4 == 1:
            p4['x'] += move
        if direction_4 == 2:
            p4['y'] += move
        if direction_4 == 3:
            p4['x'] -= move
        if direction_4 == 4:
            p4['y'] -= move

        # update the board with new player position
        draw_board()
        pygame.draw.rect(win, blue, (p1["x"], p1["y"], 10, 10))
        pygame.draw.rect(win, red, (p2["x"], p2["y"], 10, 10))
        pygame.draw.rect(win, green, (p3["x"], p3["y"], 10, 10))
        pygame.draw.rect(win, purple, (p4["x"], p4["y"], 10, 10))
        pygame.display.flip()

        # clears middle of window
        win.fill(black, (50, 50, 400, 400))
        pygame.display.flip()
        
        # if player lands on special space, they receive $100
        if player4.colliderect(special):
            p4['$'] += 100
            text = font.render('Player 4 now has', True, white)
            win.blit(text, (130, 120))
            text = font.render(str(p4['$']), True, white)
            win.blit(text, (130, 150))
            pygame.display.flip()
        wait(4)
    return

# makes window black
win.fill(black)
# draws game board
draw_board()
# displays title of game
title()
# update display
pygame.display.flip()
# wait 3 seconds
wait(3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if state == 0:
        stage_0()
    else:
        stage_1()
        '''if someone reaches $2000
        the closing screen will display and then quit'''
        if p1['$'] or p2['$'] or p3['$'] or p4['$'] == 2000:
            win.fill(black)
            font = pygame.font.SysFont('Arial', 20)
            # display player 1's money
            text = font.render('Player 1:', True, white)
            win.blit(text, (130, 120))
            text = font.render(str(p1['$']), True, white)
            win.blit(text, (200, 120))
            # display player 2's money
            text = font.render('Player 2:', True, white)
            win.blit(text, (130, 140))
            text = font.render(str(p2['$']), True, white)
            win.blit(text, (200, 140))
            if num == 3 or num == 4:
                # display player 3's money
                text = font.render('Player 3:', True, white)
                win.blit(text, (130, 160))
                text = font.render(str(p3['$']), True, white)
                win.blit(text, (200, 160))
            if num == 4:
                # display player 4's money
                text = font.render('Player 4:', True, white)
                win.blit(text, (130, 180))
                text = font.render(str(p4['$']), True, white)
                win.blit(text, (200, 180))
            pygame.display.flip()
            wait(5)
            win.fill(black)
            # whoever has at least $2000 wins
            if p1['$'] >= 2000:
                text = font.render('Player 1 wins', True, white)
                win.blit(text, (130, 120))
            if p2['$'] >= 2000:
                text = font.render('Player 2 wins', True, white)
                win.blit(text, (130, 120))
            if p3['$'] >= 2000:
                text = font.render('Player 3 wins', True, white)
                win.blit(text, (130, 120))
            if p4['$'] >= 2000:
                text = font.render('Player 4 wins', True, white)
                win.blit(text, (130, 120))
            pygame.display.flip()
            wait(5)
            font = pygame.font.Sysfont('Arial', 60)
            text = font.render('Game over', True, white)
            win.blit(text, (130, 120))
            pygame.display.flip()
            wait(5)
            sys.exit()
