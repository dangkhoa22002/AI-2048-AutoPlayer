import random

class Board:
    def __init__(self):
        self.size = 4
        # Tạo ma trận 4x4 chứa toàn số 0
        self.grid = [[0] * self.size for _ in range(self.size)]
        
        # Game bắt đầu luôn có sẵn 2 ô số
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        """
        Sinh ngẫu nhiên số 2 (90%) hoặc 4 (10%) vào ô trống bất kỳ.
        """
        empty_cells = self.get_empty_cells()
        if empty_cells:
            # Chọn ngẫu nhiên 1 tọa độ (row, col) trong các ô trống
            row, col = random.choice(empty_cells)
            # Tỷ lệ: 90% ra số 2, 10% ra số 4
            self.grid[row][col] = 2 if random.random() < 0.9 else 4

    def get_empty_cells(self):
        """
        Trả về danh sách các tọa độ (row, col) có giá trị 0.
        """
        cells = []
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    cells.append((r, c))
        return cells

    def __str__(self):
        """
        Hàm hỗ trợ in bàn cờ ra màn hình console cho dễ nhìn.
        """
        output = "-----------------\n"
        for row in self.grid:
            output += "| " + " | ".join(f"{num:^3}" for num in row) + " |\n"
        output += "-----------------"
        return output