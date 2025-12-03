# ui/colors.py

# Bảng mã màu HEX cho từng giá trị ô số
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Màu mặc định cho số lớn hơn 2048 (màu đen tuyền cho ngầu)
DEFAULT_COLOR = (60, 58, 50)

def get_color(value):
    return TILE_COLORS.get(value, DEFAULT_COLOR)