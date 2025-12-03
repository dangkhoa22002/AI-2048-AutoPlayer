import pygame
import config
from ui.colors import get_color

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("AI 2048 - Auto Player")
        
        # Font chữ
        self.title_font = pygame.font.SysFont("verdana", 50, bold=True)
        self.font = pygame.font.SysFont("verdana", 35, bold=True)
        self.btn_font = pygame.font.SysFont("verdana", 18, bold=True)
        self.label_font = pygame.font.SysFont("verdana", 16)
        self.game_over_font = pygame.font.SysFont("verdana", 60, bold=True)

        # --- SETUP BỐ CỤC (LAYOUT) ---
        self.board_origin = (30, (config.SCREEN_HEIGHT - config.BOARD_SIZE) // 2)
        panel_x = 560 # Tọa độ X bắt đầu của bảng điều khiển

        # Nút bấm
        self.reset_btn_rect = pygame.Rect(panel_x, 150, 140, 50)
        self.run_btn_rect = pygame.Rect(panel_x + 160, 150, 140, 50)

        # Radio Buttons: Mode (AI/Random)
        self.mode_random_rect = pygame.Rect(panel_x, 250, 20, 20)
        self.mode_ai_rect = pygame.Rect(panel_x + 150, 250, 20, 20)

        # Radio Buttons: Speed (Slow/Fast/Full)
        self.speed_slow_rect = pygame.Rect(panel_x, 340, 20, 20)
        self.speed_fast_rect = pygame.Rect(panel_x + 100, 340, 20, 20)
        self.speed_full_rect = pygame.Rect(panel_x + 200, 340, 20, 20)

    def draw_game(self, grid, score, high_score, ai_running, ai_mode, ai_speed_str, game_over):
        self.screen.fill(config.BACKGROUND_COLOR)
        
        self.draw_board(grid)
        self.draw_dashboard(score, high_score, ai_running, ai_mode, ai_speed_str)
        
        if game_over:
            self.draw_game_over()

        pygame.display.update()

    def draw_board(self, grid):
        start_x, start_y = self.board_origin
        
        # Vẽ nền bàn cờ
        pygame.draw.rect(self.screen, config.BOARD_COLOR, 
                         (start_x, start_y, config.BOARD_SIZE, config.BOARD_SIZE), border_radius=10)

        for r in range(4):
            for c in range(4):
                value = grid[r][c]
                # Tính toán tọa độ
                cell_x = start_x + config.GRID_PADDING + c * (config.CELL_SIZE + config.GRID_PADDING)
                cell_y = start_y + config.GRID_PADDING + r * (config.CELL_SIZE + config.GRID_PADDING)
                
                # Vẽ ô
                color = config.EMPTY_CELL_COLOR if value == 0 else get_color(value)
                pygame.draw.rect(self.screen, color, (cell_x, cell_y, config.CELL_SIZE, config.CELL_SIZE), border_radius=5)
                
                # Vẽ số
                if value != 0:
                    text_color = config.FONT_COLOR_DARK if value <= 4 else config.FONT_COLOR_LIGHT
                    # Giảm kích thước font nếu số quá to (1024, 2048)
                    font_size = 40 if value < 100 else (35 if value < 1000 else 30)
                    dynamic_font = pygame.font.SysFont("verdana", font_size, bold=True)
                    
                    text_srf = dynamic_font.render(str(value), True, text_color)
                    text_rect = text_srf.get_rect(center=(cell_x + config.CELL_SIZE/2, cell_y + config.CELL_SIZE/2))
                    self.screen.blit(text_srf, text_rect)

    def draw_dashboard(self, score, high_score, ai_running, ai_mode, ai_speed_str):
        # 1. Title
        title = self.title_font.render("2048 AI", True, config.FONT_COLOR_DARK)
        self.screen.blit(title, (560, 30))

        # 2. Score Box
        self.draw_score_box("SCORE", score, 560, 90)
        self.draw_score_box("BEST", high_score, 680, 90)

        # 3. Buttons
        self.draw_button("NEW GAME", self.reset_btn_rect, config.BUTTON_COLOR)
        
        run_color = (220, 80, 80) if ai_running else config.BUTTON_COLOR
        run_text = "STOP" if ai_running else "RUN AI"
        self.draw_button(run_text, self.run_btn_rect, run_color)

        # 4. Mode Selection
        self.draw_label("AI STRATEGY:", 560, 220)
        self.draw_radio(self.mode_random_rect, ai_mode == "Random", "Random")
        self.draw_radio(self.mode_ai_rect, ai_mode == "AI", "Smart AI")

        # 5. Speed Selection
        self.draw_label("AI SPEED:", 560, 310)
        self.draw_radio(self.speed_slow_rect, ai_speed_str == "Slow", "Slow")
        self.draw_radio(self.speed_fast_rect, ai_speed_str == "Fast", "Fast")
        self.draw_radio(self.speed_full_rect, ai_speed_str == "Full", "Full")
        
        # Hướng dẫn
        note = self.label_font.render("Press 'Q' to Quit", True, (150, 150, 150))
        self.screen.blit(note, (560, 500))

    def draw_game_over(self):
        # Tạo lớp phủ mờ
        overlay = pygame.Surface((config.BOARD_SIZE, config.BOARD_SIZE), pygame.SRCALPHA)
        overlay.fill(config.OVERLAY_COLOR)
        self.screen.blit(overlay, self.board_origin)

        # Chữ Game Over
        text = self.game_over_font.render("GAME OVER", True, config.FONT_COLOR_DARK)
        text_rect = text.get_rect(center=(self.board_origin[0] + config.BOARD_SIZE/2, 
                                          self.board_origin[1] + config.BOARD_SIZE/2))
        self.screen.blit(text, text_rect)

    # --- CÁC HÀM HỖ TRỢ VẼ (HELPER) ---
    def draw_score_box(self, label, value, x, y):
        pygame.draw.rect(self.screen, (187, 173, 160), (x, y, 100, 55), border_radius=5)
        lbl = self.label_font.render(label, True, (230, 230, 230))
        val = self.btn_font.render(str(value), True, (255, 255, 255))
        self.screen.blit(lbl, (x + 10, y + 5))
        self.screen.blit(val, (x + 10, y + 25))

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen, color, rect, border_radius=5)
        txt_surf = self.btn_font.render(text, True, (255, 255, 255))
        txt_rect = txt_surf.get_rect(center=rect.center)
        self.screen.blit(txt_surf, txt_rect)

    def draw_label(self, text, x, y):
        surf = self.btn_font.render(text, True, config.FONT_COLOR_DARK)
        self.screen.blit(surf, (x, y))

    def draw_radio(self, rect, selected, text):
        # Vẽ vòng tròn ngoài
        pygame.draw.circle(self.screen, (150, 150, 150), rect.center, 10, 2)
        if selected:
            pygame.draw.circle(self.screen, (237, 194, 46), rect.center, 6) # Chấm tròn vàng
        
        # Vẽ chữ bên cạnh
        txt_surf = self.label_font.render(text, True, config.FONT_COLOR_DARK)
        self.screen.blit(txt_surf, (rect.right + 10, rect.top - 2))