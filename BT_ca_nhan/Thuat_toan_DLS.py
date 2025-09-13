# BT tuan 04, buoi 02 mon AI
# Nguyen Van Hoai - 20110107

# Nguồn: tham khảo từ AI

import numpy as np

def is_safe(state, row, col):
    # Kiểm tra có thể đặt quân hậu tại (row, col) không
    for c in range(len(state)):   # duyệt qua các cột đã đặt hậu
        r = state[c]              # hàng tại cột c
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def goal_test(state):
    return len(state) == 8 # Đủ 8 quân hậu

def expand(state):
    # Sinh các trạng thái con
    col = len(state)  # cột tiếp theo cần đặt hậu
    successors = []
    for row in range(8):
        if is_safe(state, row, col):
            successors.append(state + [row])
    return successors

def recursive_dls(state, limit):
    # Thuật toán Recursive Depth-Limited Search
    cutoff_occurred = False

    if goal_test(state):
        return state

    elif len(state) == limit:
        return "cutoff"

    else:
        for successor in expand(state):
            result = recursive_dls(successor, limit)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result

        return "cutoff" if cutoff_occurred else "failure"

def depth_limited_search(limit):
    return recursive_dls([], limit)

def get_solution_arr():
    # Trả về một mảng 2 chiều numpy (n x n) với nghiệm n-queens
    arr = np.zeros((8, 8), dtype=int)
    if solution not in ("failure", "cutoff"):
        for col in range(len(solution)):
            row = solution[col]
            arr[row][col] = 1
    return arr

solution = depth_limited_search(8)

# print("Nghiệm của bài toán 8 quân hậu (1 = hậu, 0 = trống):")
# print(get_solution_arr())
