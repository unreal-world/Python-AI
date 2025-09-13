# BT tuan 04, buoi 01 mon AI
# Nguyen Van Hoai - 20110107

# Nguồn: tham khảo từ AI

import numpy as np
from collections import deque

N = 8  # số quân hậu

def is_safe(arr, row, col):
    # Kiểm tra có thể đặt hậu tại (row, col) không
    # Kiểm tra cột
    if 1 in arr[:row, col]:
        return False
    
    # Kiểm tra đường chéo trái trên
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if arr[r, c] == 1:
            return False
        r -= 1
        c -= 1
    
    # Kiểm tra đường chéo phải trên
    r, c = row - 1, col + 1
    while r >= 0 and c < N:
        if arr[r, c] == 1:
            return False
        r -= 1
        c += 1
    
    return True

def dfs_n_queens(n):
    # Giải bài toán n-queens bằng DFS
    stack = deque()
    stack.append((np.zeros((n, n), dtype=int), 0))  # bàn cờ rỗng + hàng 0
    
    while stack:
        arr, row = stack.pop()  # DFS: lấy phần tử cuối (LIFO)
        
        if row == n:  # đủ n quân hậu
            return arr

        for col in range(n):
            if is_safe(arr, row, col):
                new_arr = arr.copy()
                new_arr[row, col] = 1
                stack.append((new_arr, row + 1))
    
    return None

def get_solution_arr(n=8):
    # Trả về một mảng 2 chiều numpy (n x n) với nghiệm n-queens
    return dfs_n_queens(n)

# Chạy thuật toán và in nghiệm
solution = get_solution_arr()

# print("Nghiệm của bài toán 8 quân hậu (1 = hậu, 0 = trống):")
# print(solution)
