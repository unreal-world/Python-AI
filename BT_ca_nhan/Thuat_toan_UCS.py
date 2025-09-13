# BT tuan 04, buoi 02 mon AI
# Nguyen Van Hoai - 20110107

# Nguồn: tham khảo từ AI

import heapq
import numpy as np

N = 8  # số quân hậu

def is_safe(state, row, col):
    # Kiểm tra có thể đặt quân hậu tại (row, col) không
    for c in range(len(state)):
        r = state[c]
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def is_have_positions(row, col):
    # Trả về tất cả ô bị một quân hậu tại (row, col) khống chế
    positions = set()

    # hàng và cột
    for i in range(N):
        if i != col:
            positions.add((row, i))
        if i != row:
            positions.add((i, col))

    # chéo chính
    for d in range(1, N):
        if row + d < N and col + d < N:
            positions.add((row + d, col + d))
        if row - d >= 0 and col - d >= 0:
            positions.add((row - d, col - d))

    # chéo phụ
    for d in range(1, N):
        if row + d < N and col - d >= 0:
            positions.add((row + d, col - d))
        if row - d >= 0 and col + d < N:
            positions.add((row - d, col + d))

    return positions

def goal_test(state):
    return len(state) == N

def expand(state, attacked):
    # Sinh các trạng thái con từ state
    col = len(state)
    successors = []
    for row in range(N):
        if is_safe(state, row, col):
            new_positions = is_have_positions(row, col)
            # chỉ tính thêm số ô mới bị khống chế
            step_cost = len(new_positions - attacked)
            successors.append((state + [row], attacked | new_positions, step_cost))
    return successors

def uniform_cost_search():
    # UCS cho bài toán 8 quân hậu (chi phí = số ô mới bị khống chế)
    frontier = []
    heapq.heappush(frontier, (0, [], set()))  # (cost, state, attacked)
    explored = set()

    while frontier:
        cost, state, attacked = heapq.heappop(frontier)

        if goal_test(state):
            return state, cost

        explored.add(tuple(state))

        for successor, new_attacked, step_cost in expand(state, attacked):
            new_cost = cost + step_cost
            if tuple(successor) not in explored:
                heapq.heappush(frontier, (new_cost, successor, new_attacked))

    return None, float("inf")

def get_solution_arr():
    arr = np.zeros((N, N), dtype=int)
    if solution:
        for col in range(len(solution)):
            row = solution[col]
            arr[row][col] = 1
    return arr

solution, cost = uniform_cost_search()

# print("Nghiệm tìm được:", solution)
# print("Chi phí thấp nhất:", cost)
# print(get_solution_arr())
