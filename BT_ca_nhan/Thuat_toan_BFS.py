# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time
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
    # BFS giải bài toán 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    step_count = 0

    start = np.zeros((N, N), dtype=int)
    queue = deque([(start, 0)])  # (board, col)
    steps = []                   # lưu tất cả các bước

    while queue:
        board, col = queue.popleft()   # FIFO → BFS
        steps.append(board.copy())
        step_count += 1

        if col >= N:
            total_time = time.time() - start_time
            return steps, board, step_count, total_time  # tìm thấy nghiệm

        for row in range(N):
            if is_safe(board, row, col):
                new_board = board.copy()
                new_board[row][col] = 1
                queue.append((new_board, col + 1))

    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    # Lấy nghiệm cuối cùng (numpy array 8x8) hoặc None
    _, solution, _, _ = bfs()
    return solution

def get_steps():
    # Lấy tất cả steps, step_count, và thời gian
    steps, _, step_count, total_time = bfs()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
