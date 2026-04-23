import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50
player_speed = 5  # Initial player speed

# Enemy properties
enemy_size = 50
enemies = [{"pos": [random.randint(0, WIDTH - enemy_size), 0], "speed": 10}]  # List of enemies

# Load enemy image (replace 'enemy.png' with your file name)
enemy_image = pygame.image.load('rott.png').convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

# Load player image (replace 'player.png' with your file name)
player_image = pygame.image.load('bunii.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Trail properties
trail = []  # List to store previous positions
trail_length = 20  # Maximum number of trail points
trail_color = (235, 0, 0)  # Red color for the trail

# High score file
highscore_file = "highscore.txt"

# Load high score from file
if os.path.exists(highscore_file):
    with open(highscore_file, "r") as file:
        high_score = int(file.read())
else:
    high_score = 0

score = 0
game_over = False
time_elapsed = 0  # Time elapsed in milliseconds
enemy_spawn_timer = 0  # Timer for spawning new enemies

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed  # Move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed  # Move right

    # Wrap around the screen
    if player_pos[0] < 0:  # If the player goes off the left edge
        player_pos[0] = WIDTH  # Move to the right edge
    elif player_pos[0] > WIDTH:  # If the player goes off the right edge
        player_pos[0] = 0  # Move to the left edge

    # Update enemy positions
    for enemy in enemies:
        enemy["pos"][1] += enemy["speed"]

        # Resetting the Enemy
        if enemy["pos"][1] > HEIGHT:
            enemy["pos"][1] = 0
            # Spawn closer to the player's x-coordinate with some randomness
            enemy["pos"][0] = max(0, min(WIDTH - enemy_size, player_pos[0] + random.randint(-100, 100)))
            score += 1
            print(f"Score: {score}")

    # Collision Detection
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy["pos"][0], enemy["pos"][1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            print("Game Over!")
            game_over = True

    # Update trail
    trail.append((player_pos[0] + player_size // 2, player_pos[1] + player_size // 2))  # Store the center of the player
    if len(trail) > trail_length:
        trail.pop(0)  # Remove the oldest position if the trail exceeds the maximum length

    # Increase speeds over time
    time_elapsed += clock.get_time()  # Add the time since the last frame
    enemy_spawn_timer += clock.get_time()  # Track time for spawning new enemies
    if time_elapsed > 5500:  # Every 5.5 seconds
        player_speed += 2  # Increase player speed
        for enemy in enemies:
            enemy["speed"] += 2  # Increase enemy speed
        time_elapsed = 0  # Reset the timer

    # Spawn new enemies
    if enemy_spawn_timer > 15000:  # After 15 seconds, spawn the first new enemy
        enemies.append({"pos": [random.randint(0, WIDTH - enemy_size), 0], "speed": 10})
        enemy_spawn_timer = 0  # Reset the spawn timer
    elif len(enemies) > 1 and enemy_spawn_timer > 45000:  # Every 45 seconds after that
        enemies.append({"pos": [random.randint(0, WIDTH - enemy_size), 0], "speed": 10})
        enemy_spawn_timer = 0  # Reset the spawn timer

    # Drawing
    screen.fill((0, 0, 0))
    
    # Draw the trail
    for i, pos in enumerate(trail):
        alpha = int(255 * (i / trail_length))  # Calculate transparency based on position in the trail
        trail_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)  # Create a surface with alpha channel
        trail_surface.fill((*trail_color, alpha))  # Fill with the trail color and transparency
        screen.blit(trail_surface, (pos[0] - player_size // 2, pos[1] - player_size // 2))

    # Draw the enemies as images
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["pos"][0], enemy["pos"][1]))
    # Draw the player as an image
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    # Display the score and high score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))

    pygame.display.update()
    clock.tick(30)

# Update high score if the current score is greater
if score > high_score:
    high_score = score
    with open(highscore_file, "w") as file:
        file.write(str(high_score))

pygame.quit()
