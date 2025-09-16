
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
from collections import deque

N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        # kiểm tra đường chéo
        for d in range(1, col+1):
            if row-d >= 0 and board[row-d][col-d] == 1:
                return False
            if row+d < N and board[row+d][col-d] == 1:
                return False
    return True

def bfs():
    start = np.zeros((N, N), dtype=int)
    queue = deque([(start, 0)])  # (board, col)
    steps = []                   # lưu tất cả các bước

    while queue:
        board, col = queue.popleft()   # FIFO → BFS
        steps.append(board.copy())

        if col >= N:
            return steps  # tìm thấy nghiệm

        for row in range(N):
            if is_safe(board, row, col):
                new_board = board.copy()
                new_board[row][col] = 1
                queue.append((new_board, col + 1))

    return steps

def get_solution_arr():
    #Lấy nghiệm cuối cùng (mảng numpy 8x8) từ UCS.
    steps = bfs()
    if steps:
        return steps[-1]  # trạng thái cuối cùng là nghiệm
    return None

#print(get_solution_arr())
