# BT tuan 03, buoi 02 mon AI
# Nguyen Van Hoai - 20110107

import numpy as np
from collections import deque

N = 8  # số quân hậu

def is_safe(board, row, col):
    """Kiểm tra có thể đặt hậu tại (row, col) không"""
    # Kiểm tra cột
    if 1 in board[:row, col]:
        return False
    
    # Kiểm tra đường chéo trái trên
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r, c] == 1:
            return False
        r -= 1
        c -= 1
    
    # Kiểm tra đường chéo phải trên
    r, c = row - 1, col + 1
    while r >= 0 and c < N:
        if board[r, c] == 1:
            return False
        r -= 1
        c += 1
    
    return True

def bfs_n_queens(n):
    # Giải bài toán n-queens bằng BFS
    queue = deque()
    queue.append((np.zeros((n, n), dtype=int), 0))  # bàn cờ rỗng + hàng 0
    
    while queue:
        board, row = queue.popleft()
        
        if row == n:  # đủ n quân hậu
            return board
        
        for col in range(n):
            if is_safe(board, row, col):
                new_board = board.copy()
                new_board[row, col] = 1
                queue.append((new_board, row + 1))
    
    return None

def get_solution_board(n=8):
    """Trả về một mảng 2 chiều numpy (n x n) với nghiệm n-queens"""
    return bfs_n_queens(n)

# Chạy thuật toán và in nghiệm
solution = get_solution_board(N)

print("Nghiệm của bài toán 8 quân hậu (1 = hậu, 0 = trống):")
print(solution)
