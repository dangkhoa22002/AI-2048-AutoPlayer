# ai/heuristics.py
import math

# --- TRỌNG SỐ (Cấu hình theo công thức trong Checklist) ---
W_MONO = 1.0    # Trọng số tính đơn điệu
W_SMOOTH = 0.1  # Trọng số độ mượt (chênh lệch ít)
W_FREE = 2.7    # Trọng số ô trống (Rất quan trọng để không bị kẹt)
W_MAX = 1.0     # Trọng số giá trị lớn nhất

def evaluate_board(grid):
    """
    Tính điểm Score = w1*Mono + w2*Smooth + w3*Free + w4*Max
    """
    return (
        W_MONO * calculate_monotonicity(grid) +
        W_SMOOTH * calculate_smoothness(grid) +
        W_FREE * calculate_free_tiles(grid) +
        W_MAX * calculate_max_tile(grid)
    )

def calculate_free_tiles(grid):
    """Đếm số lượng ô trống (logarit để khuyến khích nhiều ô trống)"""
    empty_count = 0
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                empty_count += 1
    return empty_count if empty_count == 0 else math.log(empty_count) * 10

def calculate_max_tile(grid):
    """Lấy giá trị ô lớn nhất"""
    max_val = 0
    for r in range(4):
        for c in range(4):
            if grid[r][c] > max_val:
                max_val = grid[r][c]
    return math.log(max_val, 2) if max_val > 0 else 0

def calculate_smoothness(grid):
    """
    Độ mượt: Tổng sự chênh lệch giữa các ô kề nhau.
    Càng ít chênh lệch càng tốt (kết quả trả về số âm).
    """
    smoothness = 0
    for r in range(4):
        for c in range(4):
            if grid[r][c] != 0:
                val = math.log(grid[r][c], 2)
                # So sánh với ô bên phải
                if c < 3 and grid[r][c+1] != 0:
                    val_right = math.log(grid[r][c+1], 2)
                    smoothness -= abs(val - val_right)
                # So sánh với ô bên dưới
                if r < 3 and grid[r+1][c] != 0:
                    val_down = math.log(grid[r+1][c], 2)
                    smoothness -= abs(val - val_down)
    return smoothness

def calculate_monotonicity(grid):
    """
    Tính đơn điệu: Các con số có tăng dần/giảm dần theo hướng Trái/Phải/Lên/Xuống không.
    """
    totals = [0, 0, 0, 0] # Left/Right, Up/Down

    # Duyệt hàng ngang (Left/Right)
    for r in range(4):
        current = 0
        next_val = 0
        for c in range(3):
            current = grid[r][c]
            next_val = grid[r][c+1]
            if current > next_val:
                totals[0] += next_val - current # Phạt nếu giảm
            elif next_val > current:
                totals[1] += current - next_val # Phạt nếu tăng

    # Duyệt hàng dọc (Up/Down)
    for c in range(4):
        current = 0
        next_val = 0
        for r in range(3):
            current = grid[r][c]
            next_val = grid[r+1][c]
            if current > next_val:
                totals[2] += next_val - current
            elif next_val > current:
                totals[3] += current - next_val

    # Chọn hướng tốt nhất (ít bị phạt nhất) cho hàng ngang và dọc
    return max(totals[0], totals[1]) + max(totals[2], totals[3])