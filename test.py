import pygame
import sys
pygame.init()
all_fonts = pygame.font.get_fonts()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)
gold = (212,175,55)
win = pygame.display.set_mode((500,500))

state = 0

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

p_width = 10
p_height = 10
player1 = pygame.Rect(p1["x"],p1["y"],p_width,p_height)
player2 = pygame.Rect(p2["x"],p2["y"],p_width,p_height)
player3 = pygame.Rect(p3["x"],p3["y"],p_width,p_height)
player4 = pygame.Rect(p4["x"],p4["y"],p_width,p_height)

click = False

def player_num():
    global click
    font = pygame.font.SysFont('Arial', 20)
    # button for 2 players
    two_p = pygame.Rect(175,145,150,70)
    pygame.draw.rect(win, gold, two_p)
    text = font.render('2 players', True, black)
    win.blit(text, (210,170))
    # button for 3 players
    three_p = pygame.Rect(75,265,150,70)
    pygame.draw.rect(win, gold, three_p)
    text = font.render('3 players', True, black)
    win.blit(text, (110,290))
    # button for 4 players
    four_p = pygame.Rect(275,265,150,70)
    pygame.draw.rect(win, gold, four_p)
    text = font.render('4 players', True, black)
    win.blit(text, (310,290))
    pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if two_p.collidepoint(pygame.mouse.get_pos()):
            num = 2
            font = pygame.font.SysFont('Arial', 100)
            text = font.render(('2'), True, white)
            win.blit(text, (210,170))
            click = True
            pygame.display.flip()
        if three_p.collidepoint(pygame.mouse.get_pos()):
            num = 3
            font = pygame.font.SysFont('Arial', 100)
            text = font.render(('3'), True, white)
            win.blit(text, (210,170))
            click = True
            pygame.display.flip()
        if four_p.collidepoint(pygame.mouse.get_pos()):
            num = 4
            font = pygame.font.SysFont('Arial', 100)
            text = font.render(('4'), True, white)
            win.blit(text, (210,170))
            click = True
            pygame.display.flip()
    return
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if click == True:
            state = 1
        if state == 0:
            player_num()
            pygame.display.flip()
        if state == 1:
            pygame.time.delay(1000)
            win.fill(black, (50,50,400,400))
            pygame.display.flip()
