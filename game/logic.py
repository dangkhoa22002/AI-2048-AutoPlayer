# game/logic.py

def compress(grid):
    """Dồn số về bên trái, không thay đổi điểm số."""
    new_grid = [[0] * 4 for _ in range(4)]
    changed = False
    for r in range(4):
        pos = 0
        for c in range(4):
            if grid[r][c] != 0:
                new_grid[r][pos] = grid[r][c]
                if c != pos:
                    changed = True
                pos += 1
    return new_grid, changed

def merge(grid):
    """
    Gộp số và TRẢ VỀ ĐIỂM SỐ.
    Ví dụ: 2 gộp 2 -> Điểm += 4.
    """
    score_gained = 0
    changed = False
    for r in range(4):
        for c in range(3):
            if grid[r][c] != 0 and grid[r][c] == grid[r][c+1]:
                merged_val = grid[r][c] * 2
                grid[r][c] = merged_val
                grid[r][c+1] = 0
                
                score_gained += merged_val  # Cộng điểm
                changed = True
    return grid, changed, score_gained

def reverse(grid):
    new_grid = []
    for r in range(4):
        new_grid.append([])
        for c in range(4):
            new_grid[r].append(grid[r][3-c])
    return new_grid

def transpose(grid):
    new_grid = [[0]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            new_grid[r][c] = grid[c][r]
    return new_grid

# --- CÁC HÀM DI CHUYỂN (Cập nhật để trả về score) ---

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2, score = merge(new_grid) # Nhận điểm từ hàm merge
    new_grid, _ = compress(new_grid)
    return new_grid, (changed1 or changed2), score

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed, score = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed, score

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed, score = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed, score

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed, score = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed, score

# --- CHECK GAME OVER (Giữ nguyên) ---
def check_game_over(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0: return False
    for r in range(4):
        for c in range(3):
            if grid[r][c] == grid[r][c+1]: return False
    for r in range(3):
        for c in range(4):
            if grid[r][c] == grid[r+1][c]: return False
    return True