
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import heapq
import numpy as np

N = 8

def is_safe(state, row):
    """Kiểm tra có thể đặt quân hậu ở (col=len(state), row) không"""
    col = len(state)
    for c, r in enumerate(state):
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def count_attacks(state, row, col):
    """Đếm số ô bị loại bỏ thêm nếu đặt quân hậu ở (row, col)."""
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
    # tổng chi phí đã đặt
    return sum(costs)

def h(state):
    # số quân hậu còn lại
    return N - len(state)

def f(state, costs):
    # f(n) = g(n) + h(n)
    return g(costs) + h(state)

def state_to_numpy(state):
    """Chuyển state dạng list sang mảng numpy 8x8"""
    arr = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        arr[row, col] = 1
    return arr

def a_star_search():
    #Thuật toán A* cho 8 quân hậu.
    '''Trả về (steps, solution):
        - steps: danh sách các numpy 8x8 board
        - solution: state cuối cùng nếu tìm thấy'''
    frontier = []
    heapq.heappush(frontier, (f([], []), [], []))  # (f(n), state, costs)
    steps = []

    while frontier:
        fn, state, costs = heapq.heappop(frontier)

        # Lưu trạng thái hiện tại
        steps.append(state_to_numpy(state))

        if len(state) == N:
            return steps, state

        col = len(state)
        for row in range(N):
            if is_safe(state, row):
                cost = count_attacks(state, row, col)
                new_state = state + [row]
                new_costs = costs + [cost]
                heapq.heappush(frontier, (f(new_state, new_costs), new_state, new_costs))

    return steps, None

def get_solution_arr():
    steps, solution = a_star_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _ = a_star_search()
    return steps

#print(get_solution_arr())
