import pygame
import os
import random
import asyncio 

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Window Settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# --- ASSETS LOADING ---
# Background Music
music_path = "Purple Planet Music - Deep Mystical Lake (1_27) 120bpm.mp3"
if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
else:
    print("Music file not found, skipping music.")

# Bird Image / Placeholder
bird_path = "bird1.png"
if os.path.exists(bird_path):
    bird_img = pygame.image.load(bird_path)
    bird = pygame.transform.scale(bird_img, (40, 30))
else:
    print("Bird image not found, using yellow square.")
    bird = pygame.Surface((40, 30))
    bird.fill((255, 255, 0))

# Sounds
jump_sound = pygame.mixer.Sound("jump.wav") if os.path.exists("jump.wav") else None
game_over_sound = pygame.mixer.Sound("game_over.wav") if os.path.exists("game_over.wav") else None

# Background
bg_path = "background.png"
bg = pygame.image.load(bg_path) if os.path.exists(bg_path) else None

# --- GAME VARIABLES ---
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Global variables 
bird_x, bird_y = 50, HEIGHT // 2
velocity = 0
gravity = 0.5
jump_strength = -8
pipe_width = 60
pipe_x = WIDTH
pipe_gap = 150
pipe_height = random.randint(100, 300)
score = 0

def game_over_screen():
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    score_text = font.render(f"Your Score: {score}", True, (255, 255, 255))
    restart_text = font.render("Press R to Restart or Q to Quit", True, (200, 200, 200))
    
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 60))
    screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 40))
    
    if game_over_sound:
        game_over_sound.play()

def reset_game():
    global bird_y, velocity, score, pipe_x, pipe_height
    bird_y = HEIGHT // 2
    velocity = 0
    score = 0
    pipe_x = WIDTH
    pipe_height = random.randint(100, 300)

# --- MAIN ASYNC FUNCTION ---
async def main():
    global bird_y, velocity, score, pipe_x, pipe_height
    
    running = True
    game_active = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    velocity = jump_strength
                    if jump_sound:
                        jump_sound.play()
                
                if not game_active:
                    if event.key == pygame.K_r:
                        reset_game()
                        game_active = True
                    if event.key == pygame.K_q:
                        running = False

        if game_active:
            # Physics
            velocity += gravity
            bird_y += velocity

            # Pipe Movement
            pipe_x -= 3
            if pipe_x < -pipe_width:
                pipe_x = WIDTH
                pipe_height = random.randint(100, 300)
                score += 1

            # Rects for collision
            bird_rect = pygame.Rect(bird_x, bird_y, 40, 30)
            pipe_rect_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
            pipe_rect_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT)

            # Collision & Bounds check
            if bird_rect.colliderect(pipe_rect_top) or bird_rect.colliderect(pipe_rect_bottom) or bird_y > HEIGHT or bird_y < 0:
                game_active = False

            # Drawing
            if bg:
                screen.blit(bg, (0, 0))
            else:
                screen.fill((135, 206, 235)) # Sky Blue

            screen.blit(bird, (bird_x, bird_y))
            pygame.draw.rect(screen, (0, 200, 0), pipe_rect_top)
            pygame.draw.rect(screen, (0, 200, 0), pipe_rect_bottom)
            
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
        else:
            game_over_screen()

        pygame.display.update()
        clock.tick(30)
        
      
        await asyncio.sleep(0) 

    pygame.quit()


asyncio.run(main())