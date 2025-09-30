# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(board, row, col):
    # kiểm tra cột và chéo
    for r in range(row):
        if board[r, col] == 1:
            return False
    for d in range(1, row + 1):
        if col - d >= 0 and board[row - d, col - d] == 1:
            return False
        if col + d < N and board[row - d, col + d] == 1:
            return False
    return True

def observe(board, row, col):
    # Quan sát một phần sau khi đặt hậu.
    # Ví dụ: trả về số cột an toàn ở hàng tiếp theo.

    safe_cols = 0
    if row + 1 < N:
        for c in range(N):
            if is_safe(board, row + 1, c):
                safe_cols += 1
    return safe_cols

def dfs_partial_obs():
    # Partially Observable Search cho 8 quân hậu
    # Belief state = tập hợp các board có thể, kèm observation
    start_time = time.time()
    step_count = 0
    steps = []

    start = np.zeros((N, N), dtype=int)
    start_key = tuple(map(tuple, start))
    belief = frozenset([start_key])
    stack = [(belief, 0)]   # (belief_state, row)
    explored = set()

    while stack:
        belief_state, row = stack.pop()
        steps.append(belief_state)
        step_count += 1

        # goal test
        all_done = True
        for board_key in belief_state:
            arr = np.array(board_key, dtype=int)
            if arr.sum() != N:
                all_done = False
                break
        if all_done:
            total_time = time.time() - start_time
            solution = np.array(next(iter(belief_state)), dtype=int)
            return steps, solution, step_count, total_time

        if (belief_state, row) not in explored and row < N:
            explored.add((belief_state, row))
            new_belief = set()

            for board_key in belief_state:
                board = np.array(board_key, dtype=int)
                for col in range(N):
                    if is_safe(board, row, col):
                        new_board = board.copy()
                        new_board[row, col] = 1

                        # Thay vì lọc, chỉ ghi nhận observation
                        obs = observe(new_board, row, col)

                        # Lưu board + observation như tuple ((board), obs)
                        # Để đơn giản, ta chỉ lưu board (nhưng có thể log obs ra console)
                        # print(f"Row {row}, Col {col}, Obs={obs}")

                        new_belief.add(tuple(map(tuple, new_board)))

            if new_belief:
                stack.append((frozenset(new_belief), row + 1))

    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    _, solution, _, _ = dfs_partial_obs()
    return solution

def get_steps():
    steps, _, step_count, total_time = dfs_partial_obs()
    steps_as_arrays = []
    for belief_state in steps:
        if len(belief_state) > 0:
            board_key = next(iter(belief_state))
            board = np.array(board_key, dtype=int)
            steps_as_arrays.append(board)
    return steps_as_arrays, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
