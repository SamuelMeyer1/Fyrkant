import pygame
import sys
import random

# Initiate Pygame
pygame.init()

# Set window size
window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Samuels Spel")

# Config
coins = 0
Antalfyrkanter = 10
size = 10
x = random.randint(0, window_size[0] - size)
y = random.randint(0, window_size[1] - size)
minx = 100
miny = 100

# Mynthanteringen
countscore = Antalfyrkanter * 5

# Create a list of colors for squares
RedColor = (255, 0, 0)
BlueColor = (0, 0, 255)
GreenColor = (0, 255, 0)
colors = [RedColor, BlueColor, GreenColor]

# Function to pick a random color for the square
def randomcolor():
    return random.choice(colors)

def spawnmonster():
    size = 10
    x = random.randint(0, window_size[0] - size)
    y = random.randint(0, window_size[1] - size)
    color = randomcolor()
    print ('X')
    print (x)
    print ('Y')
    print (y)
    squares.append((x + minx, y + miny, size, size, color))

# Create five squares with random positions and colors
squares = []
for _ in range(Antalfyrkanter):
    spawnmonster()


# Function to draw a button
def draw_button():
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, 110, 50))  # Green square representing the button
    font = pygame.font.Font(None, 20)
    text = font.render("Köp fyrkant 10kr", True, (0, 0, 0))
    screen.blit(text, (10, 30))  # Place the text in the middle of the button


def buy_monster():
    global countscore
    if countscore > 0:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, size, size))
        pygame.display.update()
        #countscore = countscore - 5
        spawnmonster()
        print(' Du har köpt ett monster')
    else:
        print(' Du har inte råd')


# Main loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check if the mouse is clicked
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(30, 30, 100, 50)  # Create a rectangle around the button
            if button_rect.collidepoint(mouse_pos):  # Check if the mouse click occurred within the button boundaries
                buy_monster()

    screen.fill((0, 0, 0))  # Clear the screen
    draw_button()  # Draw the button

    # Draw squares on the screen
    for square in squares:
        pygame.draw.rect(screen, square[4], square[:4])

    # Draw coin count
    font = pygame.font.Font(None, 25)
    text = font.render(f"Coins: {countscore}", True, (255, 255, 255))
    screen.blit(text, (130, 30))

    pygame.display.update()  # Update the screen
