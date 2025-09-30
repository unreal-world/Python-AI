# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(board, row, col):
    # Kiểm tra cột
    for r in range(row):
        if board[r, col] == 1:
            return False
    # Kiểm tra 2 đường chéo
    for d in range(1, row + 1):
        if col - d >= 0 and board[row - d, col - d] == 1:
            return False
        if col + d < N and board[row - d, col + d] == 1:
            return False
    return True

def backtrack(board, row, steps, step_counter):
    step_counter[0] += 1
    steps.append(board.copy())

    if row == N:
        return True   # đã đặt đủ N quân hậu

    for col in range(N):
        if is_safe(board, row, col):
            board[row, col] = 1
            if backtrack(board, row + 1, steps, step_counter):
                return True
            board[row, col] = 0   # quay lui

    return False

def solve_backtracking():
    start_time = time.time()
    board = np.zeros((N, N), dtype=int)
    steps = []
    step_counter = [0]

    success = backtrack(board, 0, steps, step_counter)

    total_time = time.time() - start_time
    if success:
        return steps, board, step_counter[0], total_time
    else:
        return steps, None, step_counter[0], total_time

def get_solution_arr():
    _, solution, _, _ = solve_backtracking()
    return solution

def get_steps():
    steps, _, step_count, total_time = solve_backtracking()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
