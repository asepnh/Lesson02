import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello PyGame!")

# background
background = pygame.image.load("background.png")
clock = pygame.time.Clock()


class Player(object):
   def __init__(self):
       self.img = pygame.image.load("player.png")
       self.x = 370
       self.y = 480
       self.x_change = 0
       self.y_change = 0
       self.lives = 3
        
def draw_player(img, x, y):
   screen.blit(img, (x, y))

# RENDER YOUR GAME HERE
# draw the player draw_player(player.img, player.x, player.y)
# update the display
pygame.display.update()

clock.tick(60)  # limits FPS to 60


# main_loop()
running = True
while running:
    # RGB: Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0)) 
    # pool of events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
           # check for key presses
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   player.x_change = -5
               if event.key == pygame.K_RIGHT:
                   player.x_change = 5
               if event.key == pygame.K_UP:
                   player.y_change = -5
               if event.key == pygame.K_DOWN:
                   player.y_change = 5
player.x += player.x_change
player.y += player.y_change

# draw the player
draw_player(player.img, player.x, player.y)

pygame.quit()