# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import heapq
import numpy as np
import time

N = 8

def is_safe(state, col):
    """Kiểm tra có thể đặt quân hậu ở (row=len(state), col) không"""
    row = len(state)
    for r, c in enumerate(state):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def count_conflicts(state):
    # Đếm tổng số ô bị quân hậu chiếm/chạm (xung đột) trên toàn bàn
    # cho tất cả quân đã đặt.
    conflicts = set()
    for row, col in enumerate(state):
        # cùng hàng
        for c in range(N):
            if c != col:
                conflicts.add((row, c))
        # cùng cột
        for r in range(N):
            if r != row:
                conflicts.add((r, col))
        # chéo chính (\)
        for dr in range(-N, N):
            r, c = row + dr, col + dr
            if 0 <= r < N and 0 <= c < N and (r, c) != (row, col):
                conflicts.add((r, c))
        # chéo phụ (/)
        for dr in range(-N, N):
            r, c = row + dr, col - dr
            if 0 <= r < N and 0 <= c < N and (r, c) != (row, col):
                conflicts.add((r, c))
    return len(conflicts)

def h(state):
    # Heuristic: tổng số ô xung đột trên bàn
    return count_conflicts(state)

def state_to_numpy(state):
    arr = np.zeros((N, N), dtype=int)
    for row, col in enumerate(state):
        arr[row, col] = 1
    return arr

def greedy_best_first_search():
    # Greedy Best-First Search cho 8 quân hậu,
    # với heuristic là tổng số ô xung đột trên toàn bàn

    start_time = time.time()
    frontier = []
    steps = []
    step_count = 0

    # (heuristic, state)
    heapq.heappush(frontier, (h([]), []))

    while frontier:
        _, state = heapq.heappop(frontier)

        steps.append(state_to_numpy(state))
        step_count += 1

        # kiểm tra goal
        if len(state) == N:
            total_time = time.time() - start_time
            return steps, state, step_count, total_time

        row = len(state)
        for col in range(N):
            if is_safe(state, col):
                new_state = state + [col]
                heapq.heappush(frontier, (h(new_state), new_state))

    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    _, solution, _, _ = greedy_best_first_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _, step_count, total_time = greedy_best_first_search()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
