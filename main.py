import pygame
import sys
from game.board import Board
from game.logic import move_left, move_right, move_up, move_down, check_game_over
from ui.display import Display

def main():
    # 1. Khởi tạo
    game_board = Board()
    ui = Display()
    clock = pygame.time.Clock() # Để kiểm soát FPS

    print("Game Started! Use Arrow Keys to play. Press Q to Quit.")

    # 2. Vòng lặp chính (Game Loop)
    running = True
    while running:
        # A. Xử lý sự kiện (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Xử lý phím bấm
            if event.type == pygame.KEYDOWN:
                changed = False
                if event.key == pygame.K_LEFT:
                    game_board.grid, changed = move_left(game_board.grid)
                elif event.key == pygame.K_RIGHT:
                    game_board.grid, changed = move_right(game_board.grid)
                elif event.key == pygame.K_UP:
                    game_board.grid, changed = move_up(game_board.grid)
                elif event.key == pygame.K_DOWN:
                    game_board.grid, changed = move_down(game_board.grid)
                elif event.key == pygame.K_q:
                    running = False

                # Nếu có di chuyển -> Sinh số mới -> Kiểm tra thua
                if changed:
                    game_board.add_new_tile()
                    if check_game_over(game_board.grid):
                        print("GAME OVER!")

        # B. Vẽ lại màn hình (Render)
        ui.draw_board(game_board.grid)
        
        # Giới hạn tốc độ khung hình (60 FPS)
        clock.tick(60)

    # Thoát
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()