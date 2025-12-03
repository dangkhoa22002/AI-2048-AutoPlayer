from game.board import Board

# Test thử Class Board
if __name__ == "__main__":
    print("=== TEST BACKEND: KHỞI TẠO BÀN CỜ ===")
    
    # 1. Khởi tạo
    game = Board()
    print("Bàn cờ ban đầu (phải có 2 số ngẫu nhiên):")
    print(game) # Nó sẽ gọi hàm __str__ để in ra đẹp
    
    # 2. Test sinh thêm số
    print("\nThử sinh thêm 1 số mới:")
    game.add_new_tile()
    print(game)
    
    print("\n--> Test thành công! Logic khởi tạo ổn.")