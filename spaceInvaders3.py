import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Load background image
background = pygame.image.load("background.png")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Player class
class Player(object):
    def __init__(self):
        self.img = pygame.image.load("player.png")
        self.x = 370
        self.y = 480
        self.x_change = 0
        self.y_change = 0
        self.lives = 3

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Enemy class
class Alien(object):
    def __init__(self, x, y):
        # Load the original alien image
        original_img = pygame.image.load("alien.png")
        
        # Scale the image to 2.5% of its original size
        self.img = pygame.transform.scale(original_img, 
                                          (int(original_img.get_width() * 0.025), 
                                           int(original_img.get_height() * 0.025)))
        
        # Set the initial position
        self.x = x
        self.y = y
        self.x_change = 3  # Horizontal movement speed
        self.y_change = 40  # Vertical movement when hitting a boundary

    def move(self):
        # Update the alien's position
        self.x += self.x_change

        # Reverse direction and move down when hitting screen boundaries
        if self.x <= 0 or self.x >= 800 - self.img.get_width():
            self.x_change *= -1
            self.y += self.y_change

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Initialize player
player = Player()

# Initialize aliens
aliens = []
for i in range(6):  # Create 6 aliens
    alien_x = 50 + i * 100  # Space aliens evenly across the screen
    alien_y = 50
    aliens.append(Alien(alien_x, alien_y))

# Main game loop
running = True
while running:
    # Draw the background
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -5
            if event.key == pygame.K_RIGHT:
                player.x_change = 5
            if event.key == pygame.K_UP:
                player.y_change = -5
            if event.key == pygame.K_DOWN:
                player.y_change = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.x_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player.y_change = 0

    # Update player position
    player.x += player.x_change
    player.y += player.y_change

    # Ensure the player stays within screen bounds
    player.x = max(0, min(player.x, 800 - player.img.get_width()))
    player.y = max(0, min(player.y, 600 - player.img.get_height()))

    # Move and draw the aliens
    for alien in aliens:
        alien.move()
        alien.draw()

    # Draw the player
    player.draw()

    # Update the display
    pygame.display.update()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()