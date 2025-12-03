import pygame
import sys
import config
from game.board import Board
from game.logic import move_left, move_right, move_up, move_down, check_game_over
from ui.display import Display

# --- IMPORT MỚI TỪ THƯ MỤC AI ---
from ai.algorithms import get_random_move, get_best_move 
# --------------------------------

def main():
    game_board = Board()
    ui = Display()
    clock = pygame.time.Clock()
    
    score = 0
    high_score = 0
    game_over = False 
    
    ai_running = False
    ai_mode = "Random"
    
    # Tốc độ AI
    ai_speed_str = "Fast" 
    fps = config.SPEED_FAST

    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except: pass

    running = True
    while running:
        # A. XỬ LÝ SỰ KIỆN (Giữ nguyên như cũ)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                with open("highscore.txt", "w") as f: f.write(str(high_score))
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos
                    if ui.reset_btn_rect.collidepoint(pos):
                        game_board = Board()
                        score = 0
                        game_over = False
                        ai_running = False 
                    if ui.run_btn_rect.collidepoint(pos) and not game_over:
                        ai_running = not ai_running
                    if ui.mode_random_rect.collidepoint(pos): ai_mode = "Random"
                    if ui.mode_ai_rect.collidepoint(pos): ai_mode = "AI"
                    
                    # Chỉnh FPS theo speed
                    if ui.speed_slow_rect.collidepoint(pos): 
                        ai_speed_str = "Slow"
                        fps = config.SPEED_SLOW
                        print("Speed set to SLOW")

                    if ui.speed_fast_rect.collidepoint(pos): 
                        ai_speed_str = "Fast"
                        fps = config.SPEED_FAST
                        print("Speed set to FAST")

                    if ui.speed_full_rect.collidepoint(pos): 
                        ai_speed_str = "Full"
                        fps = config.SPEED_FULL
                        print("Speed set to FULL") 

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

        # B. AI LOGIC (SỬA LẠI ĐỂ DÙNG MODULE MỚI)
        if ai_running and not game_over:
            pygame.event.pump() # Chống treo máy
            
            move_func = None
            
            if ai_mode == "Random":
                # Gọi hàm từ file ai/algorithms.py
                move_func = get_random_move(game_board.grid)
                
            elif ai_mode == "AI":
                # Gọi hàm Expectimax xịn xò
                move_func = get_best_move(game_board.grid, depth=3)  #Đã thay đổi từ depth 2 lên 4 và hiểu quả rõ rệt, nhưng để 3 cho an toàn tránh treo máy
            
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
                    # Nếu AI tính ra nước đi nhưng thực tế không đổi (hiếm gặp), dừng AI
                    if ai_mode == "AI": 
                        pass 

        # C. RENDER
        ui.draw_game(game_board.grid, score, high_score, ai_running, ai_mode, ai_speed_str, game_over)
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()