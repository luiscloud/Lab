import pygame, sys, random
from pygame.locals import *

#CONSTANTS
WINDOWWIDTH = 640
WINDOWHEIGHT = 360
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60
BULLETSPEED = 4
BULLETLENGTH = 10
PLAYERWIDTH = 40
PLAYERHEIGHT = 100
PLAYERX = 50
PLAYERY = 210
GRAVITY = 0.2
JUMPVELOCITY = 10
AMMO = 3

# Player Profiles
PLAYERCOLOR = [(255, 0, 0), (0, 255, 0)]

# Player Variables
player = [pygame.Rect(PLAYERX, PLAYERY, PLAYERWIDTH, PLAYERHEIGHT)] + [pygame.Rect(640 - (PLAYERX + PLAYERWIDTH), PLAYERY, PLAYERWIDTH, PLAYERHEIGHT)]
bullets = [[], []]
jumpState = [False, False]
jumpTime = [0, 0]

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Pressing ESC quits.
                    terminate()
                return

def playerHit(playerRect, bullets):
    for b in bullets:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def aiEngine(bullets):
    keyStoke = ''
    return keyStoke

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('DuelAI')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# Set up sounds.
# gameOverSound = pygame.mixer.Sound('gameover.wav')
# pygame.mixer.music.load('background.mid')

# Set up images.
# playerImage = pygame.image.load('player.png')
# playerRect = playerImage.get_rect()
# baddieImage = pygame.image.load('baddie.png')

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
drawText('DuelAI', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

while True:
    # Set up the start of the game.


    while True: # The game loop runs while the game part is playing.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.key == K_SPACE:
                print('jump')
                jumpState[0] = True
                # jump
            if event.key == K_f:
                print('fire')
                if playerAmmo[0] > 0:
                    playerAmmo[0] -= 1
                    bullets[0] += [pygame.Rect(90, player[0].top + 50, 10, 2)]
                # fire

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)

        # Draw each bullet

        pygame.display.update()

        # Check if any of the bullets have hit a player.


        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    # pygame.mixer.music.stop()
    # gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface,
           (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    # gameOverSound.stop()