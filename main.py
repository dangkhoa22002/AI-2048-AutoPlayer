import pygame
import sys
import random
import config 
from game.board import Board
from game.logic import move_left, move_right, move_up, move_down, check_game_over
from ui.display import Display

def get_random_move():
    return random.choice([move_left, move_right, move_up, move_down])

def main():
    game_board = Board()
    ui = Display()
    clock = pygame.time.Clock()
    
    # State Variables
    score = 0
    high_score = 0
    game_over = False 
    
    ai_running = False
    ai_mode = "Random"
    
    # Tốc độ AI (Mặc định Fast)
    ai_speed_str = "Fast" 
    fps = config.SPEED_FAST

    # Load High Score
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except: pass

    running = True
    while running:
        # A. INPUT EVENT (XỬ LÝ SỰ KIỆN)
        for event in pygame.event.get():
            
            # 1. LOGIC THOÁT GAME (Ưu tiên cao nhất)
            # Bấm nút X trên cửa sổ HOẶC Bấm phím Q
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # Lưu điểm cao trước khi thoát
                with open("highscore.txt", "w") as f: 
                    f.write(str(high_score))
                running = False
            
            # 2. CLICK CHUỘT (Xử lý nút bấm UI)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos
                    
                    # Nút RESET
                    if ui.reset_btn_rect.collidepoint(pos):
                        game_board = Board()
                        score = 0
                        game_over = False
                        ai_running = False 
                        print("Game Reset!")

                    # Nút RUN/STOP (Chỉ bấm được nếu chưa Game Over)
                    if ui.run_btn_rect.collidepoint(pos) and not game_over:
                        ai_running = not ai_running

                    # Chọn Mode
                    if ui.mode_random_rect.collidepoint(pos): ai_mode = "Random"
                    if ui.mode_ai_rect.collidepoint(pos): ai_mode = "AI"

                    # Chọn Speed
                    if ui.speed_slow_rect.collidepoint(pos): 
                        ai_speed_str = "Slow"
                        fps = config.SPEED_SLOW
                    if ui.speed_fast_rect.collidepoint(pos): 
                        ai_speed_str = "Fast"
                        fps = config.SPEED_FAST
                    if ui.speed_full_rect.collidepoint(pos): 
                        ai_speed_str = "Full"
                        fps = config.SPEED_FULL

            # 3. PHÍM ĐIỀU HƯỚNG (Chỉ nhận khi AI tắt và chưa Game Over)
            elif not ai_running and not game_over and event.type == pygame.KEYDOWN:
                move_func = None
                if event.key == pygame.K_LEFT: move_func = move_left
                elif event.key == pygame.K_RIGHT: move_func = move_right
                elif event.key == pygame.K_UP: move_func = move_up
                elif event.key == pygame.K_DOWN: move_func = move_down
                
                if move_func:
                    new_grid, changed, points = move_func(game_board.grid)
                    if changed:
                        game_board.grid = new_grid
                        game_board.add_new_tile()
                        score += points
                        if score > high_score: high_score = score
                        if check_game_over(game_board.grid): game_over = True

        # B. AI LOGIC
        if ai_running and not game_over:
            pygame.event.pump() # Giúp Windows biết game vẫn đang sống
            move_func = None
            if ai_mode == "Random":
                move_func = get_random_move()
            elif ai_mode == "AI":
                # Placeholder cho Minimax
                move_func = get_random_move() 
            
            if move_func:
                new_grid, changed, points = move_func(game_board.grid)
                if changed:
                    game_board.grid = new_grid
                    game_board.add_new_tile()
                    score += points
                    if score > high_score: high_score = score
                    if check_game_over(game_board.grid): 
                        game_over = True
                        ai_running = False 
                else:
                    pass

        # C. RENDER
        ui.draw_game(game_board.grid, score, high_score, ai_running, ai_mode, ai_speed_str, game_over)
        
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()