import pygame
import sys
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

def save_data():
    """
    Placeholder function for saving EEG data.
    Implement data saving logic here.
    """
    pass  # To be implemented later

def main():
    # Initialize BrainFlow
    BoardShim.enable_dev_board_logger()
    params = BrainFlowInputParams()
    board_id = BoardIds.SYNTHETIC_BOARD.value
    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream()
    print("BrainFlow streaming started...")

    # Initialize Pygame
    pygame.init()
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption("Motor Imagery Task")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Fonts
    large_font = pygame.font.SysFont(None, 200)
    medium_font = pygame.font.SysFont(None, 100)
    small_font = pygame.font.SysFont(None, 50)

    # Control Variables
    running = True
    in_menu = True
    in_input = False
    in_trial_menu = False
    direction = 'left'  # Start with 'left' and alternate
    trial_number = 1
    total_trials = 10  # Default number of trials

    # Bar Settings
    green_bar_width = 20
    green_bar_height = 200
    loading_bar_thickness = 30
    arrow_offset_y = 100  # Move arrow up by 100 pixels

    # Positions for Green Bars
    left_green_bar_pos = (100, infoObject.current_h // 2 - green_bar_height // 2)
    right_green_bar_pos = (infoObject.current_w - 100 - green_bar_width, infoObject.current_h // 2 - green_bar_height // 2)

    # Center Position
    center_pos = (infoObject.current_w // 2, infoObject.current_h // 2)

    # Clock
    clock = pygame.time.Clock()

    # Input Variables
    input_text = ""
    input_error = False

    while running:
        if in_menu:
            # Display Main Menu
            screen.fill(BLACK)
            title_text = large_font.render("EEG Motor Imagery", True, WHITE)
            start_text = medium_font.render("Press S to Start", True, GREEN)
            set_text = medium_font.render("Press N to Set Number", True, WHITE)
            quit_text = medium_font.render("Press Q to Quit", True, RED)
            trials_text = small_font.render(f"Total Trials: {total_trials}", True, WHITE)

            # Positioning Text
            title_rect = title_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 4))
            start_rect = start_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 - 50))
            set_rect = set_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 + 50))
            quit_rect = quit_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 + 150))
            trials_rect = trials_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 - 150))

            # Blit Text to Screen
            screen.blit(title_text, title_rect)
            screen.blit(start_text, start_rect)
            screen.blit(set_text, set_rect)
            screen.blit(quit_text, quit_rect)
            screen.blit(trials_text, trials_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        in_menu = False
                    elif event.key == pygame.K_n:
                        in_input = True
                        in_menu = False
                        input_text = ""
                        input_error = False
                    elif event.key == pygame.K_q:
                        running = False

        elif in_input:
            # Display Input Menu for Setting Number of Trials
            screen.fill(BLACK)
            prompt_text = medium_font.render("Enter Number of Recordings (Even):", True, WHITE)
            input_display = medium_font.render(input_text, True, GREEN if not input_error else RED)
            instructions_text = small_font.render("Press Enter to Confirm", True, WHITE)

            # Positioning Text
            prompt_rect = prompt_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 3))
            input_rect = input_display.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2))
            instructions_rect = instructions_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 + 100))

            # Blit Text to Screen
            screen.blit(prompt_text, prompt_rect)
            screen.blit(input_display, input_rect)
            screen.blit(instructions_text, instructions_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    elif event.key == pygame.K_RETURN:
                        if input_text.isdigit():
                            entered_number = int(input_text)
                            if entered_number > 0:
                                if entered_number % 2 != 0:
                                    entered_number += 1  # Make it even
                                    input_error = True
                                total_trials = entered_number
                                in_input = False
                                in_menu = True
                            else:
                                input_error = True
                        else:
                            input_error = True
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.unicode.isdigit():
                        input_text += event.unicode

        elif in_trial_menu:
            # Display Trial Menu (Accessible via 'M' during trials)
            screen.fill(BLACK)
            menu_title = medium_font.render("Trial Menu", True, WHITE)
            quit_text = medium_font.render("Press Q to Quit", True, RED)
            resume_text = medium_font.render("Press R to Resume", True, GREEN)

            # Positioning Text
            menu_title_rect = menu_title.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 3))
            quit_rect = quit_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2))
            resume_rect = resume_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 + 100))

            # Blit Text to Screen
            screen.blit(menu_title, menu_title_rect)
            screen.blit(quit_text, quit_rect)
            screen.blit(resume_text, resume_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_r:
                        in_trial_menu = False

        else:
            # Display Current Trial Number
            screen.fill(BLACK)
            # Redraw green bars
            pygame.draw.rect(screen, GREEN, (*left_green_bar_pos, green_bar_width, green_bar_height))
            pygame.draw.rect(screen, GREEN, (*right_green_bar_pos, green_bar_width, green_bar_height))

            # Draw Current Trial Info
            trial_info = small_font.render(f"Trial {trial_number}/{total_trials}", True, WHITE)
            trial_info_rect = trial_info.get_rect(topright=(infoObject.current_w - 50, 50))
            screen.blit(trial_info, trial_info_rect)

            # Draw Focus Period '+' sign
            plus_text = large_font.render("+", True, WHITE)
            plus_rect = plus_text.get_rect(center=center_pos)
            screen.blit(plus_text, plus_rect)
            pygame.display.flip()

            # Collect data during focus period
            focus_duration = 3  # seconds
            focus_start_time = time.time()
            while time.time() - focus_start_time < focus_duration:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            break
                # Placeholder for data collection during focus
                save_data()
                clock.tick(60)

            if not running:
                break

            # Show Arrow (Moved Up)
            arrow_length = 100
            arrow_color = WHITE
            arrow_width = 20
            arrow_y_offset = arrow_offset_y  # Move arrow up by arrow_offset_y pixels

            # Clear screen but keep green bars and trial info
            screen.fill(BLACK)
            # Redraw green bars
            pygame.draw.rect(screen, GREEN, (*left_green_bar_pos, green_bar_width, green_bar_height))
            pygame.draw.rect(screen, GREEN, (*right_green_bar_pos, green_bar_width, green_bar_height))
            # Redraw trial info
            screen.blit(trial_info, trial_info_rect)

            # Draw Arrow
            if direction == 'left':
                pygame.draw.polygon(screen, arrow_color, [
                    (center_pos[0] - arrow_length, center_pos[1] - arrow_y_offset),
                    (center_pos[0], center_pos[1] - arrow_y_offset - arrow_width),
                    (center_pos[0], center_pos[1] - arrow_y_offset + arrow_width)
                ])
            else:
                pygame.draw.polygon(screen, arrow_color, [
                    (center_pos[0] + arrow_length, center_pos[1] - arrow_y_offset),
                    (center_pos[0], center_pos[1] - arrow_y_offset - arrow_width),
                    (center_pos[0], center_pos[1] - arrow_y_offset + arrow_width)
                ])
            pygame.display.flip()

            # Wait before starting the loading bar
            pre_loading_duration = 1  # second
            pre_loading_start = time.time()
            while time.time() - pre_loading_start < pre_loading_duration:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            break
                clock.tick(60)

            if not running:
                break

            # Loading Bar
            loading_duration = 7  # seconds
            loading_start_time = time.time()

            while time.time() - loading_start_time < loading_duration:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            break
                        elif event.key == pygame.K_m:
                            in_trial_menu = True
                            break

                # Calculate loading bar progress
                elapsed_time = time.time() - loading_start_time
                loading_progress = elapsed_time / loading_duration

                screen.fill(BLACK)
                # Redraw green bars
                pygame.draw.rect(screen, GREEN, (*left_green_bar_pos, green_bar_width, green_bar_height))
                pygame.draw.rect(screen, GREEN, (*right_green_bar_pos, green_bar_width, green_bar_height))
                # Redraw trial info
                screen.blit(trial_info, trial_info_rect)

                # Redraw Arrow
                if direction == 'left':
                    pygame.draw.polygon(screen, arrow_color, [
                        (center_pos[0] - arrow_length, center_pos[1] - arrow_y_offset),
                        (center_pos[0], center_pos[1] - arrow_y_offset - arrow_width),
                        (center_pos[0], center_pos[1] - arrow_y_offset + arrow_width)
                    ])
                    # Calculate current length of the loading bar
                    # From center to left green bar
                    max_length = center_pos[0] - (left_green_bar_pos[0] + green_bar_width)
                    current_length = loading_progress * max_length

                    # Draw loading bar moving left from center
                    pygame.draw.rect(screen, WHITE, (
                        center_pos[0] - current_length,  # Start at center and move left
                        center_pos[1] - loading_bar_thickness // 2,
                        current_length,
                        loading_bar_thickness
                    ))
                else:
                    pygame.draw.polygon(screen, arrow_color, [
                        (center_pos[0] + arrow_length, center_pos[1] - arrow_y_offset),
                        (center_pos[0], center_pos[1] - arrow_y_offset - arrow_width),
                        (center_pos[0], center_pos[1] - arrow_y_offset + arrow_width)
                    ])
                    # Calculate current length of the loading bar
                    # From center to right green bar
                    max_length = (right_green_bar_pos[0]) - center_pos[0]
                    current_length = loading_progress * max_length

                    # Draw loading bar moving right from center
                    pygame.draw.rect(screen, WHITE, (
                        center_pos[0],  # Start at center and move right
                        center_pos[1] - loading_bar_thickness // 2,
                        current_length,
                        loading_bar_thickness
                    ))

                pygame.display.flip()
                # Placeholder for data collection during loading
                save_data()
                clock.tick(60)

            if not running:
                break

            # Optional rest period with accessible menu
            rest_duration = 2  # seconds
            rest_start_time = time.time()
            while time.time() - rest_start_time < rest_duration:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            break
                        elif event.key == pygame.K_m:
                            in_trial_menu = True
                            break

                # Display Rest Text with Menu Instruction
                screen.fill(BLACK)
                # Redraw green bars
                pygame.draw.rect(screen, GREEN, (*left_green_bar_pos, green_bar_width, green_bar_height))
                pygame.draw.rect(screen, GREEN, (*right_green_bar_pos, green_bar_width, green_bar_height))
                # Redraw trial info
                screen.blit(trial_info, trial_info_rect)

                rest_text = small_font.render("Rest (Press M for Menu)", True, WHITE)
                rest_rect = rest_text.get_rect(center=center_pos)
                screen.blit(rest_text, rest_rect)
                pygame.display.flip()
                clock.tick(60)

            if not running:
                break

            # Alternate Direction
            direction = 'right' if direction == 'left' else 'left'
            trial_number += 1

            # Check if all trials are completed
            if trial_number > total_trials:
                # Display a completion message
                screen.fill(BLACK)
                completion_text = medium_font.render("All Trials Completed!", True, GREEN)
                completion_rect = completion_text.get_rect(center=center_pos)
                screen.blit(completion_text, completion_rect)
                pygame.display.flip()
                # Wait for 3 seconds before returning to menu
                time.sleep(3)
                trial_number = 1  # Reset trial number
                in_menu = True

    # Handle Trial Menu outside the main loop to avoid missing quit events
        while in_trial_menu and running:
            # Display Trial Menu (Accessible via 'M' during trials)
            screen.fill(BLACK)
            menu_title = medium_font.render("Trial Menu", True, WHITE)
            quit_text = medium_font.render("Press Q to Quit", True, RED)
            resume_text = medium_font.render("Press R to Resume", True, GREEN)

            # Positioning Text
            menu_title_rect = menu_title.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 3))
            quit_rect = quit_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2))
            resume_rect = resume_text.get_rect(center=(infoObject.current_w // 2, infoObject.current_h // 2 + 100))

            # Blit Text to Screen
            screen.blit(menu_title, menu_title_rect)
            screen.blit(quit_text, quit_rect)
            screen.blit(resume_text, resume_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    in_trial_menu = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        in_trial_menu = False
                    elif event.key == pygame.K_r:
                        in_trial_menu = False

    # Cleanup
    board.stop_stream()
    board.release_session()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
