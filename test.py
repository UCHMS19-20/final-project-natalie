import pygame
import sys
white = (255,255,255)
black = (0,0,0)
win = pygame.display.set_mode((500,500))
p1 = {
    'x': 0,
    'y': 0,
    '$': 0
}
p2 = {
    'x': 20,
    'y': 0,
    '$': 0
}
p3 = {
    'x': 0,
    'y': 20,
    '$': 0
}
p4 = {
    'x': 20,
    'y': 20,
    '$': 0
}

while True : 
    p1['$'] += 2100
    win.fill (black)
    font = pygame.font.SysFont('Arial', 20)
    text = font.render('Player 1:', True, white)
    win.blit(text, (130,120))
    text = font.render(str(p1['$']), True, white)
    win.blit(text, (130,150))
    text = font.render('Player 2:', True, white)
    win.blit(text, (130,120))
    text = font.render(str(p2['$']), True, white)
    win.blit(text, (130,150))
    text = font.render('Player 3:', True, white)
    win.blit(text, (130,120))
    text = font.render(str(p3['$']), True, white)
    win.blit(text, (130,150))
    text = font.render('Player 4:', True, white)
    win.blit(text, (130,120))
    text = font.render(str(p4['$']), True, white)
    win.blit(text, (130,150))
    pygame.time.delay(5000)
    win.fill(black)
    if p1['$'] >= 2000:
        text = font.render('Player 1 wins', True, white)
        win.blit(text, (130,120))
    if p2['$'] >= 2000:
        text = font.render('Player 2 wins', True, white)
        win.blit(text, (130,120))
    if p3['$'] >= 2000:
        text = font.render('Player 3 wins', True, white)
        win.blit(text, (130,120))
    if p4['$'] >= 2000:
        text = font.render('Player 4 wins', True, white)
        win.blit(text, (130,120))
    pygame.display.update()
    pygame.time.delay(5000)
