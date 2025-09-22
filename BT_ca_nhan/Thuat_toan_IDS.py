# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(state, row, col):
    for c in range(len(state)):
        r = state[c]
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def goal_test(state):
    return len(state) == N

def state_to_board(state):
    # Chuyển state (list vị trí hàng cho từng cột) thành mảng 8x8
    board = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        board[row][col] = 1
    return board

def expand(state):
    col = len(state)
    successors = []
    for row in range(N):
        if is_safe(state, row, col):
            successors.append(state + [row])
    return successors

def recursive_dls(state, limit, steps, step_counter):
    # Lưu lại trạng thái hiện tại
    steps.append(state_to_board(state))
    step_counter[0] += 1  # tăng bộ đếm

    if goal_test(state):
        return state

    elif len(state) == limit:
        return "cutoff"

    else:
        cutoff_occurred = False
        for successor in expand(state):
            result = recursive_dls(successor, limit, steps, step_counter)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result
        return "cutoff" if cutoff_occurred else "failure"

def depth_limited_search(limit, steps, step_counter):
    return recursive_dls([], limit, steps, step_counter)

def iterative_deepening_search():
    # IDS cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    depth = 0
    steps = []
    step_counter = [0]

    while True:
        result = depth_limited_search(depth, steps, step_counter)
        if result not in ("cutoff", "failure"):
            total_time = time.time() - start_time
            return steps, state_to_board(result), step_counter[0], total_time
        depth += 1

def get_solution_arr():
    # Lấy nghiệm cuối cùng (numpy array 8x8) hoặc None
    _, solution, _, _ = iterative_deepening_search()
    return solution

def get_steps():
    # Lấy tất cả steps, step_count và thời gian
    steps, _, step_count, total_time = iterative_deepening_search()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
