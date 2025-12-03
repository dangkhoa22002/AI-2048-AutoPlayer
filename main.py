from game.board import Board
from game.logic import move_left, move_right, move_up, move_down, check_game_over

def print_grid(grid):
    for row in grid:
        print(row)
    print("-" * 20)

if __name__ == "__main__":
    # 1. Tạo bàn cờ giả định để test (thay vì random)
    game = Board()
    # Gán cứng giá trị để test logic gộp: [2, 2, 0, 0] -> [4, 0, 0, 0]
    game.grid = [
        [2, 2, 4, 4],
        [0, 2, 2, 0],
        [4, 0, 4, 2],
        [0, 0, 0, 2]
    ]
    
    print("Bàn cờ ban đầu:")
    print_grid(game.grid)

    print("--- Thử đi sang TRÁI (LEFT) ---")
    new_grid, changed = move_left(game.grid)
    print_grid(new_grid)
    print(f"Có thay đổi không? {changed}") 
    # Kết quả mong đợi: Hàng 1 thành [4, 8, 0, 0], changed=True

    print("--- Thử đi sang PHẢI (RIGHT) với bàn cờ gốc ---")
    new_grid, changed = move_right(game.grid)
    print_grid(new_grid)
    
    # Test Game Over
    print("Check Game Over (False là chưa thua):", check_game_over(new_grid))