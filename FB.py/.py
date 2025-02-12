import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Load background music (replace with your music file path)
background_music = "Purple Planet Music - Deep Mystical Lake (1_27) 120bpm.mp3"  # Update this with your actual music file
if os.path.exists(background_music):
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely

# Set up the game window
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Load bird image
bird_path = r"C:\Users\DELL\OneDrive\Flappy_Bird\FB.py\bird1.png"
if not os.path.exists(bird_path):
    print(f"Error: {bird_path} does not exist.")
    exit()
bird = pygame.image.load(bird_path)
bird = pygame.transform.scale(bird, (40, 30))

# Load sounds (replace with your sound file paths if available)
jump_sound = pygame.mixer.Sound("jump.wav") if os.path.exists("jump.wav") else None
game_over_sound = pygame.mixer.Sound("game_over.wav") if os.path.exists("game_over.wav") else None

# Bird properties
bird_x, bird_y = 50, HEIGHT // 2
velocity = 0
gravity = 0.5
jump_strength = -8

# Pipe properties
pipe_width = 60
pipe_x = WIDTH
pipe_gap = 150
pipe_height = random.randint(100, 300)

# Background properties (optional, replace with your background image)
bg_path = "background.png"
bg = pygame.image.load(bg_path) if os.path.exists(bg_path) else None
bg_x = 0

# Score counter
score = 0
font = pygame.font.Font(None, 36)

# Game clock
clock = pygame.time.Clock()

# Function to show the game over screen
def game_over():
    screen.fill((0, 0, 0))  # Black background
    game_over_text = font.render("Game Over!", True, (255, 255, 255))  # White text
    score_text = font.render(f"Your Score: {score}", True, (255, 255, 255))
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
    screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.update()
    if game_over_sound:
        game_over_sound.play()
    pygame.time.wait(3000)  # Wait for 3 seconds before closing

# Restart or quit loop
def restart_or_quit():
    while True:
        screen.fill((0, 0, 0))
        restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Main game loop
running = True
while running:
    # Scrolling background
    if bg:
        bg_x -= 2
        if bg_x <= -WIDTH:
            bg_x = 0
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + WIDTH, 0))
    else:
        screen.fill((135, 206, 250))  # Light blue background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = jump_strength  # Jump
                if jump_sound:
                    jump_sound.play()

    # Apply gravity and update bird position
    velocity += gravity
    bird_y += velocity

    # Keep bird within the screen bounds
    if bird_y < 0:
        bird_y = 0
        velocity = 0
    if bird_y + 30 > HEIGHT:
        bird_y = HEIGHT - 30
        velocity = 0

    # Update bird rectangle for collision
    bird_rect = pygame.Rect(bird_x, bird_y, 40, 30)

    # Move pipes
    pipe_x -= 3
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_gap = random.randint(120, 180)  # Randomize gap size
        pipe_height = random.randint(100, 300)
        score += 1

    # Create Rect objects for the pipes
    pipe_rect_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    pipe_rect_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT)

    # Collision detection
    if bird_rect.colliderect(pipe_rect_top) or bird_rect.colliderect(pipe_rect_bottom):
        game_over()
        if restart_or_quit():
            bird_y, velocity, score = HEIGHT // 2, 0, 0
            pipe_x, pipe_gap = WIDTH, 150
            continue
        else:
            running = False

    # Draw the bird
    screen.blit(bird, (bird_x, bird_y))

    # Draw pipes
    pygame.draw.rect(screen, (0, 255, 0), pipe_rect_top)
    pygame.draw.rect(screen, (0, 255, 0), pipe_rect_bottom)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()


