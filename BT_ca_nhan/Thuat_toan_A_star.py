# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import heapq
import numpy as np
import time

N = 8

def is_safe(state, row):
    # Kiểm tra có thể đặt quân hậu ở (col=len(state), row) không
    col = len(state)
    for c, r in enumerate(state):
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def count_conflicts(state, row, col):
    # Đếm số ô bị loại bỏ thêm nếu đặt quân hậu ở (row, col).
    attacked = 0
    for c in range(col+1, N):
        attacked += 1  # cùng hàng
        dr = c - col
        if 0 <= row - dr < N:
            attacked += 1
        if 0 <= row + dr < N:
            attacked += 1
    return attacked

def g(costs):
    # Tổng chi phí đã đặt
    return sum(costs)

def h(state):
    # Heuristic: số quân hậu còn lại
    return N - len(state)

def f(state, costs):
    # f(n) = g(n) + h(n)
    return g(costs) + h(state)

def state_to_numpy(state):
    # Chuyển state dạng list sang mảng numpy 8x8
    arr = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        arr[row, col] = 1
    return arr

def a_star_search():
    # Thuật toán A* cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    frontier = []
    steps = []
    step_count = 0

    # (f(n), state, costs)
    heapq.heappush(frontier, (f([], []), [], []))

    while frontier:
        fn, state, costs = heapq.heappop(frontier)

        # Lưu trạng thái hiện tại
        steps.append(state_to_numpy(state))
        step_count += 1

        if len(state) == N:
            total_time = time.time() - start_time
            return steps, state, step_count, total_time

        col = len(state)
        for row in range(N):
            if is_safe(state, row):
                cost = count_conflicts(state, row, col)
                new_state = state + [row]
                new_costs = costs + [cost]
                heapq.heappush(frontier, (f(new_state, new_costs), new_state, new_costs))

    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    # Trả về solution dạng numpy array hoặc None
    _, solution, _, _ = a_star_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    # Trả về toàn bộ steps, step_count và total_time
    steps, _, step_count, total_time = a_star_search()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
