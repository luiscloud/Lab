import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 640
WINDOWHEIGHT = 360
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Duel')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
TEXTCOLOR = (0, 0, 0)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up the player and bullet data structures.
count = 0
p = 0
playerWidth = 40
playerHeight = 100
player = [pygame.Rect(50, 210, playerWidth, playerHeight)] + [pygame.Rect(550, 210, playerWidth, playerHeight)]
playerColor = [BLACK, GREEN]
playerAmmo = [3, 3]
bullets = [[],[]]
bulletSpeed = 4
bulletLength = 10
bulletHeight = 2
playerWindow = []
gamePlay = True

# Set up movement variables.
jumpState = [False, False]
jumpTime = [0, 0]

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_SPACE:
                print('jump')
                jumpState[0] = True
                #jump
            if event.key == K_f:
                print('fire')
                if playerAmmo[0] > 0:
                    playerAmmo[0] -= 1
                    bullets[0] += [pygame.Rect(90, player[0].top + 50, 10, 2)]
                #fire

    #runAI


    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.
    while p < 2:
        if jumpState[p]:
            if player[p].bottom <= 310:
                player[p].bottom = 310 - 12*jumpTime[p] + 0.2 * jumpTime[p]**2
                print('hel')
                jumpTime[p] += 1
                if player[p].bottom > 310:
                    player[p].bottom = 310
                    jumpState[p] = False
                    jumpTime[p] = 0
                    print('lo')
        p += 1

    p = 0

    # Draw the player onto the surface.
    while p < 2:
        pygame.draw.rect(windowSurface, playerColor[p], player[p])
        p += 1

    count = 0
    p = 0

    # Draw the bullet.
    while p < 2:
        while count < len(bullets[p]):
            pygame.draw.rect(windowSurface, GREEN, bullets[p][count])
            if p == 0:
                if bullets[p][count].right < WINDOWWIDTH:
                    bullets[p][count].right += bulletSpeed
                else:
                    del bullets[p][count]
                    playerAmmo[p] += 1
            if p == 1:
                if bullets[p][count].left > 0:
                    bullets[p][count].left -= bulletSpeed
                else:
                    del bullets[p][count]
                    playerAmmo[p] += 1
            count += 1
        p += 1
        count = 0

    count = 0
    p = 0

    # Check whether a player is hit.
    while p < 2 and gamePlay:
        while count < len(bullets[p]) and gamePlay:
            if p == 0:
                if bullets[p][count].colliderect(player[1]):
                    print('hit')
                    print('Game over')
                    del bullets[p][count]
                    playerAmmo[p] += 1
                    gamePlay = False
            if p == 1:
                print('n')
                #other
            count += 1
        p += 1
        count = 0

    count = 0
    p = 0

    if not gamePlay:
        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(60)