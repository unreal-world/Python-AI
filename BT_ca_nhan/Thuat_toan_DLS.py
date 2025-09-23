# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(state, row, col):
    # Kiểm tra có thể đặt quân hậu tại (row, col) không
    for c in range(len(state)):   # duyệt qua các cột đã đặt hậu
        r = state[c]              # hàng tại cột c #Ví dụ: state = [0, 4] nghĩa là: cột 0 đặt hậu ở hàng 0, cột 1 đặt hậu ở hàng 4.
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def goal_test(state):
    return len(state) == N  # đủ N quân hậu

def state_to_board(state):
    # Chuyển state (list vị trí hàng cho từng cột) thành mảng 8x8
    board = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        board[row][col] = 1
    return board

def recursive_dls(state, limit, steps, step_counter):
    # Recursive DLS: luôn lưu lại trạng thái hiện tại vào steps.
    steps.append(state_to_board(state))
    step_counter[0] += 1  # tăng bộ đếm bước

    if goal_test(state):
        return state

    elif len(state) == limit:
        return "cutoff"

    else:
        cutoff_occurred = False
        for row in range(N):
            if is_safe(state, row, len(state)):
                result = recursive_dls(state + [row], limit, steps, step_counter)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != "failure":
                    return result
        return "cutoff" if cutoff_occurred else "failure"

def dls(limit):
    # Depth Limited Search cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    steps = []
    step_counter = [0]  # dùng list để tham chiếu trong đệ quy

    result = recursive_dls([], limit, steps, step_counter)

    total_time = time.time() - start_time
    if result not in ("failure", "cutoff"):
        return steps, state_to_board(result), step_counter[0], total_time
    else:
        return steps, None, step_counter[0], total_time

def get_solution_arr():
    # Lấy nghiệm cuối cùng (numpy array 8x8) hoặc None
    _, solution, _, _ = dls(N)
    return solution

def get_steps():
    # Lấy tất cả steps, step_count và thời gian
    steps, _, step_count, total_time = dls(N)
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
