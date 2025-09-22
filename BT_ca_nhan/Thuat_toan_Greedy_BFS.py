# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import heapq
import numpy as np
import time

N = 8

def is_safe(state, col):
    # Kiểm tra có thể đặt quân hậu ở (row=len(state), col) không
    row = len(state)
    for r, c in enumerate(state):  # state lưu cột ứng với từng hàng
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def count_attacks(state, row, col):
    # Đếm số ô bị loại bỏ thêm nếu đặt quân hậu ở (row, col).
    attacked = 0
    for r in range(row+1, N):
        attacked += 1  # cùng cột
        dr = r - row
        if 0 <= col - dr < N:
            attacked += 1
        if 0 <= col + dr < N:
            attacked += 1
    return attacked

def h(state, costs):
    # Hàm heuristic: Greedy chỉ nhìn chi phí gần nhất
    if not costs:
        return 0
    return costs[-1]

def state_to_numpy(state):
    # Chuyển state (list cột theo từng hàng) sang mảng 8x8
    arr = np.zeros((N, N), dtype=int)
    for row, col in enumerate(state):
        arr[row, col] = 1
    return arr

def greedy_best_first_search():
    # Greedy Best-First Search cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    frontier = []
    steps = []
    step_count = 0

    # (h(n), state, costs)
    heapq.heappush(frontier, (0, [], []))  
    
    while frontier:
        hn, state, costs = heapq.heappop(frontier)
        
        # Lưu trạng thái đang xét
        steps.append(state_to_numpy(state))
        step_count += 1

        # kiểm tra goal
        if len(state) == N:
            total_time = time.time() - start_time
            return steps, state, step_count, total_time
        
        row = len(state)
        for col in range(N):
            if is_safe(state, col):
                cost = count_attacks(state, row, col)
                new_state = state + [col]
                new_costs = costs + [cost]
                heapq.heappush(frontier, (h(new_state, new_costs), new_state, new_costs))
    
    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    # Trả về solution dạng numpy array hoặc None
    _, solution, _, _ = greedy_best_first_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    # Trả về toàn bộ steps, step_count và total_time
    steps, _, step_count, total_time = greedy_best_first_search()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
