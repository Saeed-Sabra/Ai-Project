import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the Pygame window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers - Difficulty")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the difficulty levels
levels = {1: "Easy", 2: "Medium", 3: "Hard", 4: "Expert", 5: "Impossible"}

# Set up the initial difficulty level
current_level = 1


# Define the function to draw the start page
def draw_start_page():
    # Clear the screen
    window.fill(BLACK)

    # Draw the title
    title = font.render("Select Difficulty", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, 100))
    window.blit(title, title_rect)

    # Draw the current difficulty level
    level_text = font.render(
        "Level " + str(current_level) + " - " + levels[current_level], True, WHITE
    )
    level_rect = level_text.get_rect(center=(WIDTH / 2, 250))
    window.blit(level_text, level_rect)

    # Draw the instructions
    instructions = font.render(
        "Use the left and right arrow keys to select a difficulty level", True, WHITE
    )
    instructions_rect = instructions.get_rect(center=(WIDTH / 2, 400))
    window.blit(instructions, instructions_rect)

    # Draw the "Start" button
    start_button = font.render("Start", True, WHITE)
    start_button_rect = start_button.get_rect(center=(WIDTH / 2, 500))
    pygame.draw.rect(window, BLACK, start_button_rect.inflate(20, 20))
    window.blit(start_button, start_button_rect)

    # Update the display
    pygame.display.update()


# Call the draw_start_page function
draw_start_page()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_level = max(current_level - 1, 1)
                draw_start_page()
            elif event.key == pygame.K_RIGHT:
                current_level = min(current_level + 1, 5)
                draw_start_page()
            elif event.key == pygame.K_RETURN:
                # Start the game with the selected difficulty level
                print("Starting game with difficulty level", current_level)
                running = False

# Quit Pygame
pygame.quit()
