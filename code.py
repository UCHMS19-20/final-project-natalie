import pygame
# initiate pygame
pygame.init()

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

# update display
pygame.display.flip()

# # function for number of players
# def player_num(num):
#     if num is 2:
#         x = 0
#         y = 0
#         chip = pygame.draw.rect(win, blue, (x,y,5,5))
#         x = 10
#         y = 0
#         chip = pygame.draw.rect(win, red, (x,y,5,5))
#     if num is 3:
#         x = 0
#         y = 0
#         chip = pygame.draw.rect(win, blue, (x,y,5,5))
#         x = 10
#         y = 0
#         chip = pygame.draw.rect(win, red, (x,y,5,5))
#         x = 0
#         y = 10
#         chip = pygame.draw.rect(win, green, (x,y,5,5))
#     if num is 4:
#         x = 0
#         y = 0
#         chip = pygame.draw.rect(win, blue, (x,y,5,5))
#         x = 10
#         y = 0
#         chip = pygame.draw.rect(win, red, (x,y,5,5))
#         x = 0
#         y = 10
#         chip = pygame.draw.rect(win, green, (x,y,5,5))
#         x = 10
#         y = 10
#         chip = pygame.draw.rect(win, purple, (x,y,5,5))
#     return

# # get number of players and display chips accordingly
# player_num(input('''How many people are playing? 2 to 4 players
#     '''))

# # update display
# pygame.display.flip()

# # main loop
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
