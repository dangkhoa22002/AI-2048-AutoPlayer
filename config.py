# config.py

# --- KÍCH THƯỚC & BỐ CỤC ---
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
BOARD_SIZE = 500
GRID_PADDING = 12

# [QUAN TRỌNG] Công thức tính kích thước ô vuông dựa trên kích thước bàn cờ
# (500px trừ đi 5 khoảng trống padding) chia cho 4 ô
CELL_SIZE = (BOARD_SIZE - (GRID_PADDING * 5)) // 4

# --- TỐC ĐỘ AI (FPS) ---
SPEED_SLOW = 5   # Chậm để quan sát
SPEED_FAST = 20  # Nhanh vừa
SPEED_FULL = 120 # Tốc độ ánh sáng (để train nhanh)

# --- BẢNG MÀU (COLORS) ---
BACKGROUND_COLOR = (250, 248, 239) # Màu kem nền toàn màn hình
BOARD_COLOR = (187, 173, 160)      # Màu nền khu vực bàn cờ
EMPTY_CELL_COLOR = (205, 193, 180) # Màu ô trống

# Màu chữ
FONT_COLOR_DARK = (119, 110, 101)  # Xám đậm (cho số 2, 4)
FONT_COLOR_LIGHT = (249, 246, 242) # Trắng (cho số lớn)

# Màu UI (Nút bấm)
BUTTON_COLOR = (143, 122, 102)     # Nâu đất
BUTTON_HOVER_COLOR = (160, 140, 120)
OVERLAY_COLOR = (238, 228, 218, 180) # Màu phủ mờ khi Game Over (có độ trong suốt)
SCORE_BOX_COLOR = (187, 173, 160) # Màu nền ô điểm số