import random
import copy
import math
from game.logic import move_left, move_right, move_up, move_down
from ai.heuristics import evaluate_board

MOVES = [move_left, move_right, move_up, move_down]

# --- S-RANK UPGRADE: KHỞI TẠO BỘ NHỚ CACHE ---
# Key: Trạng thái bàn cờ (tuple), Value: (depth, score)
transposition_table = {}

def board_to_tuple(grid):
    """
    Chuyển ma trận list thành tuple để làm key cho dictionary (hashable).
    List không thể làm key, Tuple thì được.
    """
    return tuple(tuple(row) for row in grid)

def get_random_move(grid):
    """Chọn bừa 1 nước đi (Dùng cho Random Bot)"""
    return random.choice(MOVES)

def get_best_move(grid, depth=2):
    best_score = -math.inf
    best_move = None
    
    # Xóa cache cũ mỗi lần đi nước mới để tránh tốn RAM quá nhiều
    transposition_table.clear() 
    
    # Sắp xếp thứ tự nước đi: Thử đi các hướng "ngon ăn" trước (Heuristic cao)
    # Kỹ thuật này gọi là "Move Ordering" - Giúp cắt tỉa nhanh hơn
    possible_moves = []
    for move_func in MOVES:
        new_grid, changed, _ = move_func(grid)
        if changed:
            # Tính sơ bộ điểm heuristic để sắp xếp
            initial_score = evaluate_board(new_grid)
            possible_moves.append((initial_score, move_func, new_grid))
            
    # Sắp xếp giảm dần theo điểm sơ bộ
    possible_moves.sort(key=lambda x: x[0], reverse=True)

    # Duyệt qua các nước đi đã sắp xếp
    for _, move_func, new_grid in possible_moves:
        score = expectimax(new_grid, depth - 1, is_maximizing=False)
        if score > best_score:
            best_score = score
            best_move = move_func
    
    return best_move

def expectimax(grid, depth, is_maximizing):
    # 1. Kiểm tra Cache (Transposition Table)
    state_key = board_to_tuple(grid)
    if state_key in transposition_table:
        cached_depth, cached_score = transposition_table[state_key]
        # Nếu kết quả trong kho được tính với độ sâu lớn hơn hoặc bằng hiện tại -> Dùng luôn
        if cached_depth >= depth:
            return cached_score

    # 2. Base Case
    if depth == 0:
        score = evaluate_board(grid)
        return score

    if is_maximizing:
        # --- MAX NODE ---
        max_score = -math.inf
        can_move = False
        
        for move_func in MOVES:
            new_grid, changed, _ = move_func(grid)
            if changed:
                can_move = True
                score = expectimax(new_grid, depth - 1, is_maximizing=False)
                max_score = max(max_score, score)
        
        final_score = max_score if can_move else -math.inf
        
    else:
        # --- CHANCE NODE (S-RANK OPTIMIZATION) ---
        empty_cells = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
        
        if not empty_cells:
            return evaluate_board(grid)

        # Optimization: Nếu quá nhiều ô trống, chỉ xét tối đa 3 ô ngẫu nhiên
        # Để đảm bảo tốc độ khi depth cao
        if len(empty_cells) > 3:
            cells_to_check = random.sample(empty_cells, 3)
        else:
            cells_to_check = empty_cells

        total_score = 0
        weight_sum = 0
        
        for r, c in cells_to_check:
            # Xét trường hợp ra số 2 (Trọng số 0.9)
            grid_2 = copy.deepcopy(grid)
            grid_2[r][c] = 2
            total_score += 0.9 * expectimax(grid_2, depth - 1, is_maximizing=True)
            weight_sum += 0.9
            
            # Xét trường hợp ra số 4 (Trọng số 0.1)
            # Chỉ xét số 4 khi depth còn cao, nếu depth thấp bỏ qua để nhanh
            if depth > 1:
                grid_4 = copy.deepcopy(grid)
                grid_4[r][c] = 4
                total_score += 0.1 * expectimax(grid_4, depth - 1, is_maximizing=True)
                weight_sum += 0.1
        
        final_score = total_score / weight_sum

    # 3. Lưu vào Cache trước khi trả về
    transposition_table[state_key] = (depth, final_score)
    return final_score