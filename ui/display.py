import pygame
import config
from ui.colors import get_color

class Display:
    def __init__(self):
        pygame.init()
        # Tạo cửa sổ game
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("AI 2048 - Auto Player")
        
        # Khởi tạo font chữ
        self.font = pygame.font.SysFont("arial", 40, bold=True)
        self.score_font = pygame.font.SysFont("arial", 30, bold=True)

    def draw_board(self, grid):
        """Vẽ toàn bộ bàn cờ dựa trên ma trận grid"""
        self.screen.fill(config.BACKGROUND_COLOR) # Tô màu nền
        
        # Vẽ tiêu đề và điểm số (tạm thời để 0)
        title_text = self.score_font.render("AI 2048 PROJECT", True, (255, 255, 255))
        self.screen.blit(title_text, (20, 20))

        # Tính toán vị trí bắt đầu vẽ lưới (căn giữa)
        start_x = (config.SCREEN_WIDTH - config.BOARD_SIZE) // 2
        start_y = 150 # Cách lề trên 1 khoảng

        # Vẽ nền của bàn cờ (Hình vuông lớn)
        pygame.draw.rect(self.screen, (160, 140, 130), 
                         (start_x, start_y, config.BOARD_SIZE, config.BOARD_SIZE), border_radius=10)

        # Duyệt qua 4x4 ô để vẽ từng ô nhỏ
        for r in range(4):
            for c in range(4):
                value = grid[r][c]
                
                # Tính tọa độ x, y của ô nhỏ
                x = start_x + config.GRID_PADDING + c * (config.CELL_SIZE + config.GRID_PADDING)
                y = start_y + config.GRID_PADDING + r * (config.CELL_SIZE + config.GRID_PADDING)
                
                # Vẽ ô vuông
                color = config.EMPTY_CELL_COLOR if value == 0 else get_color(value)
                pygame.draw.rect(self.screen, color, (x, y, config.CELL_SIZE, config.CELL_SIZE), border_radius=5)
                
                # Vẽ số lên trên ô (nếu khác 0)
                if value != 0:
                    # Chọn màu chữ: Số nhỏ (2,4) màu xám đậm, số lớn màu trắng
                    text_color = config.FONT_COLOR if value <= 4 else config.FONT_COLOR_LIGHT
                    
                    text_surface = self.font.render(str(value), True, text_color)
                    text_rect = text_surface.get_rect(center=(x + config.CELL_SIZE//2, y + config.CELL_SIZE//2))
                    self.screen.blit(text_surface, text_rect)

        # Cập nhật màn hình
        pygame.display.update()