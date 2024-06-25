import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Avoid the Obstacles")

# Set up the player
player_size = 50
player_pos = [width/2, height-player_size*2]
player_color = (255, 255, 255)

# Set up the obstacle
obstacle_size = 50
obstacle_pos = [random.randint(0, width-obstacle_size), 0]
obstacle_color = (255, 0, 0)
obstacle_speed = 10

# Set up the score
score = 0
font = pygame.font.SysFont(None, 35)

# Set up the game loop
game_over = False
clock = pygame.time.Clock()

# Define functions
def display_score(score):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, [0, 0])

def draw_player(player_pos):
    pygame.draw.rect(window, player_color, (player_pos[0], player_pos[1], player_size, player_size))

def draw_obstacle(obstacle_pos):
    pygame.draw.rect(window, obstacle_color, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

def move_obstacle(obstacle_pos):
    obstacle_pos[1] += obstacle_speed
    if obstacle_pos[1] > height:
        obstacle_pos[0] = random.randint(0, width-obstacle_size)
        obstacle_pos[1] = 0
    return obstacle_pos

def detect_collision(player_pos, obstacle_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    o_x = obstacle_pos[0]
    o_y = obstacle_pos[1]

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obstacle_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obstacle_size)):
            return True
    return False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_pos[1] -= player_size*2

    # Update game objects
    player_pos[1] += 5
    obstacle_pos = move_obstacle(obstacle_pos)

    # Check for collisions
    if detect_collision(player_pos, obstacle_pos):
        game_over = True
        break

    # Draw game objects
    window.fill((0, 0, 0))
    draw_player(player_pos)
    draw_obstacle(obstacle_pos)
    display_score(score)
    score += 1
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
