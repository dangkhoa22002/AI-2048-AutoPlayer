# 🎮 AI 2048 Auto-Player

> Đồ án môn học Trí Tuệ Nhân Tạo
> Hệ thống tự động chơi game 2048 sử dụng thuật toán Expectimax và Heuristic nâng cao.

![Demo Screenshot](demo.png)
_(Hình ảnh minh họa giao diện game)_

## 🌟 Tính năng nổi bật

- **Game Engine:** Tự xây dựng logic 2048 và giao diện đồ họa bằng **Pygame**.
- **AI Algorithm:** Sử dụng thuật toán **Expectimax** (độ sâu tùy chỉnh) để xử lý yếu tố ngẫu nhiên của game.
- **S-Rank Optimization:**
  - **Transposition Table:** Kỹ thuật lưu vết (Caching) giúp tránh tính toán lặp lại.
  - **Heuristics:** Đánh giá bàn cờ dựa trên 4 tiêu chí: _Monotonicity, Smoothness, Free Tiles, Max Value_.
- **Giao diện trực quan:**
  - Dashboard điều khiển (Start/Stop/Reset).
  - Tùy chỉnh tốc độ (Slow/Fast/Full).
  - Lưu điểm cao (High Score).
- **Portable:** Chơi ngay không cần cài đặt Python.

---

## 📥 TẢI VÀ CHƠI NGAY

### 👨‍💻 CHƠI NGAY NHANH GỌN

Bạn không cần biết lập trình, chỉ cần tải game về và chơi:

1.  Truy cập mục **[Releases](../../releases)** bên phải giao diện GitHub.
2.  Tải file **`AI_2048_VIP.exe`**.
3.  Bấm đúp vào file để chạy. (Game sẽ tự tạo file `highscore.txt` để lưu điểm của bạn).

### 👨‍💻 TẢI CẢ DỰ ÁN

Yêu cầu: Python 3.10 trở lên.

1.  **Clone dự án:**

    ```bash
    git clone https://github.com/dangkhoa22002/AI-2048-AutoPlayer.git
    cd AI-2048-AutoPlayer
    ```

2.  **Cài đặt thư viện:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Chạy game:**
    ```bash
    python main.py
    ```

## 🎮 Hướng dẫn sử dụng

- **Chế độ Người chơi:** Sử dụng các phím mũi tên `⬅️` `➡️` `⬆️` `⬇️` để di chuyển.
- **Chế độ AI:**
  - Chọn **"Smart AI"** trên bảng điều khiển.
  - Chọn tốc độ (khuyên dùng **Fast** hoặc **Full**).
  - Bấm nút **RUN AUTO**.
- **Thoát game:** Bấm phím `Q` hoặc nút `X` trên cửa sổ.

---

## 🌟 Hướng dẫn Đóng gói (.exe)

Nếu bạn muốn tự tạo file `.exe` từ mã nguồn, hãy làm theo các bước sau:

**Bước 1: Cài đặt PyInstaller**
(Nếu bạn đã cài `requirements.txt` thì bỏ qua bước này)

```bash
pip install pyinstaller
```

**Bước 2: Chạy lệnh đóng gói Tại thư mục gốc của dự án (nơi có file main.py), chạy lệnh:**

```bash
pyinstaller --noconsole --onefile --name="AI_2048_VIP" main.py
```

**Bước 3: Lấy thành phẩm Sau khi chạy xong, file game AI_2048_VIP.exe sẽ xuất hiện trong thư mục dist/.**
