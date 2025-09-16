
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np

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
    #Chuyển state (list vị trí hàng cho từng cột) thành mảng 8x8"""
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

def recursive_dls(state, limit, steps):
    # Lưu lại trạng thái hiện tại
    steps.append(state_to_board(state))

    if goal_test(state):
        return state

    elif len(state) == limit:
        return "cutoff"

    else:
        cutoff_occurred = False
        for successor in expand(state):
            result = recursive_dls(successor, limit, steps)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result
        return "cutoff" if cutoff_occurred else "failure"

def depth_limited_search(limit, steps):
    return recursive_dls([], limit, steps)

def iterative_deepening_search():
    depth = 0
    steps = []
    while True:
        result = depth_limited_search(depth, steps)
        if result not in ("cutoff", "failure"):
            return steps, result
        depth += 1

def get_solution_arr():
    steps, result = iterative_deepening_search()
    if result not in ("failure", "cutoff"):
        return steps[-1]  # Trả về trạng thái cuối cùng
    return None

def get_steps():
    steps, _ = iterative_deepening_search()
    return steps

#print(get_solution_arr())