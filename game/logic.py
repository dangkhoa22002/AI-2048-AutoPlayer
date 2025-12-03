# game/logic.py

def compress(grid):
    """
    Dồn số về bên trái (loại bỏ số 0).
    Trả về: (ma trận mới, có thay đổi hay không)
    """
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
    Gộp 2 số giống nhau kề nhau.
    Trả về: (ma trận mới, có thay đổi hay không)
    """
    changed = False
    for r in range(4):
        for c in range(3):
            if grid[r][c] != 0 and grid[r][c] == grid[r][c+1]:
                grid[r][c] *= 2
                grid[r][c+1] = 0
                changed = True
    return grid, changed

def reverse(grid):
    """Đảo ngược hàng (Dùng cho Move Right)"""
    new_grid = []
    for r in range(4):
        new_grid.append([])
        for c in range(4):
            new_grid[r].append(grid[r][3-c])
    return new_grid

def transpose(grid):
    """Hoán vị hàng thành cột (Dùng cho Move Up/Down)"""
    new_grid = [[0]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            new_grid[r][c] = grid[c][r]
    return new_grid

# --- 4 HÀM DI CHUYỂN CHÍNH (Đã tối ưu biến changed) ---

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    new_grid, _ = compress(new_grid) # Nén lại lần nữa sau khi gộp
    return new_grid, (changed1 or changed2)

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

# --- HÀM KIỂM TRA GAME OVER (Mới thêm) ---

def check_game_over(grid):
    """
    Trả về True nếu không còn nước đi nào hợp lệ.
    """
    # 1. Nếu còn ô trống -> Chưa thua
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                return False
    
    # 2. Nếu còn 2 ô cạnh nhau giống nhau -> Chưa thua
    for r in range(4):
        for c in range(3):
            if grid[r][c] == grid[r][c+1]:
                return False
    for r in range(3):
        for c in range(4):
            if grid[r][c] == grid[r+1][c]:
                return False
    
    # Không còn cách nào cứu vãn
    return True