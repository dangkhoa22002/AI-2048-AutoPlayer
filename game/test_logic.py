# game/test_logic.py
import unittest
from logic import move_left, compress, merge

class TestGameLogic(unittest.TestCase):
    
    def test_compress(self):
        """Test hàm nén số (dồn sang trái)"""
        grid = [
            [0, 2, 0, 2],
            [0, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 4, 0]
        ]
        expected = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 0],
            [4, 0, 0, 0]
        ]
        new_grid, changed = compress(grid)
        self.assertEqual(new_grid, expected)
        self.assertTrue(changed)

    def test_merge_simple(self):
        """Test gộp cơ bản: [2, 2, 0, 0] -> [4, 0, 0, 0]"""
        grid = [[2, 2, 0, 0], [0]*4, [0]*4, [0]*4]
        expected_grid = [[4, 0, 0, 0], [0]*4, [0]*4, [0]*4]
        
        # Hàm merge trả về 3 giá trị: grid, changed, score
        new_grid, changed, score = merge(grid)
        self.assertEqual(new_grid, expected_grid)
        self.assertEqual(score, 4)

    def test_merge_complex(self):
        """
        Test trường hợp khó trong Checklist: 
        Hàng [2, 2, 2, 2] gộp sang trái phải ra [4, 4, 0, 0]
        Chứ không phải [8, 0, 0, 0]
        """
        # Mô phỏng quá trình move_left: Compress -> Merge -> Compress
        row = [2, 2, 2, 2]
        grid = [row, [0]*4, [0]*4, [0]*4]
        
        # 1. Compress (không đổi vì đã dồn rồi)
        
        # 2. Merge
        # [2, 2, 2, 2] -> [4, 0, 4, 0] (Gộp cặp 1-2 và cặp 3-4)
        merged_grid, _, _ = merge(grid)
        
        # 3. Compress lần 2
        # [4, 0, 4, 0] -> [4, 4, 0, 0]
        final_grid, _ = compress(merged_grid)
        
        expected_row = [4, 4, 0, 0]
        self.assertEqual(final_grid[0], expected_row)

if __name__ == '__main__':
    unittest.main()