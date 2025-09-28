# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(board, row, col):
    # board: numpy array shape (N,N)
    # kiểm tra cùng cột bên trên
    for r in range(row):
        if board[r, col] == 1:
            return False
    # kiểm tra 2 đường chéo hướng lên trên
    for d in range(1, row + 1):
        if col - d >= 0 and board[row - d, col - d] == 1:
            return False
        if col + d < N and board[row - d, col + d] == 1:
            return False
    return True

def dfs():
    # Searching with No Observations (DFS) cho 8 quân hậu.
    # Action: đặt một quân hậu vào hàng `row` tại cột hợp lệ.
    # Belief state: frozenset of board-keys, board-key = tuple of tuples.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    step_count = 0
    steps = []

    start = np.zeros((N, N), dtype=int)
    start_key = tuple(map(tuple, start))          # hashable representation
    initial_belief = frozenset([start_key])       # belief = tập các board có thể
    stack = [(initial_belief, 0)]                 # (belief_state, row)
    explored = set()                              # lưu (belief_state, row) đã thăm

    while stack:
        belief_state, row = stack.pop()   # DFS LIFO
        steps.append(belief_state)
        step_count += 1

        # goal test: tất cả board trong belief state đều có N quân hậu
        all_done = True
        for board_key in belief_state:
            arr = np.array(board_key, dtype=int)
            if arr.sum() != N:
                all_done = False
                break

        if all_done:
            total_time = time.time() - start_time
            # trả về một board làm nghiệm (lấy board đầu tiên trong belief)
            board_key = next(iter(belief_state))
            solution = np.array(board_key, dtype=int)
            return steps, solution, step_count, total_time

        # tiếp tục mở rộng nếu chưa thăm và row < N
        if (belief_state, row) not in explored and row < N:
            explored.add((belief_state, row))

            # tạo belief mới bằng cách đặt hậu ở hàng 'row' cho từng board trong belief
            new_belief = set()
            for board_key in belief_state:
                board = np.array(board_key, dtype=int)
                for col in range(N):
                    if is_safe(board, row, col):
                        new_board = board.copy()
                        new_board[row, col] = 1
                        new_belief.add(tuple(map(tuple, new_board)))

            if new_belief:
                stack.append((frozenset(new_belief), row + 1))

    total_time = time.time() - start_time
    return steps, None, step_count, total_time


def get_solution_arr():
    _, solution, _, _ = dfs()
    return solution


def get_steps():
    steps, _, step_count, total_time = dfs()

    # Chuyển đổi belief state -> numpy array
    steps_as_arrays = []
    for belief_state in steps:
        if len(belief_state) > 0:
            board_key = next(iter(belief_state))      # lấy 1 board đại diện
            board = np.array(board_key, dtype=int)
            steps_as_arrays.append(board)

    return steps_as_arrays, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
