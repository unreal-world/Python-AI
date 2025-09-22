# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8
K = 40  # beam width

def is_safe(state, col):
    # Kiểm tra có thể đặt quân hậu ở (row=len(state), col) không
    row = len(state)
    for r, c in enumerate(state):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def heuristic(state):
    # Đánh giá heuristic: số quân hậu đã đặt (càng nhiều càng tốt)
    return len(state)

def state_to_numpy(state):
    """Chuyển state (list cột theo từng hàng) sang mảng 8x8"""
    arr = np.zeros((N, N), dtype=int)
    for row, col in enumerate(state):
        arr[row, col] = 1
    return arr

def beam_search():
    # Thuật toán Beam Search cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()

    steps = []
    frontier = [[]]  # mỗi state là list cột
    step_count = 0

    while frontier:
        candidates = []
        for state in frontier:
            steps.append(state_to_numpy(state))
            step_count += 1
            if len(state) == N:
                elapsed = time.time() - start_time
                return steps, state, step_count, elapsed
            row = len(state)
            for col in range(N):
                if is_safe(state, col):
                    new_state = state + [col]
                    candidates.append(new_state)
        # chọn K state tốt nhất dựa trên heuristic
        candidates.sort(key=lambda s: heuristic(s), reverse=True)
        frontier = candidates[:K]

    elapsed = time.time() - start_time
    return steps, None, step_count, elapsed

def get_solution_arr():
    # Chỉ trả về solution dạng numpy array hoặc None
    _, solution, _, _ = beam_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    # Trả về toàn bộ steps, số bước và thời gian
    steps, _, step_count, total_time = beam_search()
    return steps, step_count, total_time


if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
