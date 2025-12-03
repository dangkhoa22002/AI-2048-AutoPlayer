# config.py

# Kích thước màn hình
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700  # Cao hơn chút để chứa điểm số
BOARD_SIZE = 500     # Kích thước bàn cờ vuông 4x4
GRID_PADDING = 10    # Khoảng cách giữa các ô

# Màu sắc nền
BACKGROUND_COLOR = (187, 173, 160) # Màu nâu nhạt đặc trưng của 2048
EMPTY_CELL_COLOR = (205, 193, 180) # Màu ô trống
FONT_COLOR = (119, 110, 101)       # Màu chữ số nhỏ (2, 4)
FONT_COLOR_LIGHT = (249, 246, 242) # Màu chữ số lớn (8, 16...)

# Tính toán kích thước ô dựa trên padding
CELL_SIZE = (BOARD_SIZE - (GRID_PADDING * 5)) // 4