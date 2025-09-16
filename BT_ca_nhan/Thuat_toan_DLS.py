
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np

N = 8

def is_safe(state, row, col):
    # Kiểm tra có thể đặt quân hậu tại (row, col) không
    for c in range(len(state)):   # duyệt qua các cột đã đặt hậu
        r = state[c]              # hàng tại cột c
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def goal_test(state):
    return len(state) == N  # đủ N quân hậu

def state_to_board(state):
    #Chuyển state (list vị trí hàng cho từng cột) thành mảng 8x8
    board = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        board[row][col] = 1
    return board

def recursive_dls(state, limit, steps):
    #Recursive DLS: luôn lưu lại trạng thái hiện tại vào steps.
    #steps: danh sách chứa các numpy array (mỗi array là 1 bàn cờ).
    # Lưu trạng thái hiện tại
    steps.append(state_to_board(state))

    if goal_test(state):
        return state

    elif len(state) == limit:
        return "cutoff"

    else:
        cutoff_occurred = False
        for row in range(N):
            if is_safe(state, row, len(state)):
                result = recursive_dls(state + [row], limit, steps)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != "failure":
                    return result
        return "cutoff" if cutoff_occurred else "failure"

def dls(limit):
    steps = []
    result = recursive_dls([], limit, steps)
    return steps, result

def get_solution_arr():
    steps, result = dls(N)
    if result not in ("failure", "cutoff"):
        return steps[-1]  # trạng thái cuối cùng
    return None

def get_steps():
    steps, _ = dls(N)
    return steps

#print(get_solution_arr())