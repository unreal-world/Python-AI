
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import heapq
import numpy as np

N = 8

def is_safe(state, col):
    #Kiểm tra có thể đặt quân hậu ở (row=len(state), col) không
    row = len(state)
    for r, c in enumerate(state):  # state lưu cột ứng với từng hàng
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def count_attacks(state, row, col):
    #Đếm số ô bị loại bỏ thêm nếu đặt quân hậu ở (row, col).
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
    if not costs:
        return 0
    return costs[-1]  # Greedy chỉ nhìn chi phí gần nhất

def state_to_numpy(state):
    """Chuyển state (list cột theo từng hàng) sang mảng 8x8"""
    arr = np.zeros((N, N), dtype=int)
    for row, col in enumerate(state):
        arr[row, col] = 1
    return arr

def greedy_best_first_search():
    #Greedy Best First Search cho 8 quân hậu (theo hàng).
    '''Trả về (steps, solution):
      - steps: danh sách các board (numpy 8x8) theo thứ tự xét
      - solution: state cuối cùng nếu tìm thấy'''
    frontier = []
    steps = []
    heapq.heappush(frontier, (0, [], []))  # (h(n), state, costs)
    
    while frontier:
        hn, state, costs = heapq.heappop(frontier)
        
        # Lưu trạng thái đang xét
        steps.append(state_to_numpy(state))
        
        # kiểm tra goal
        if len(state) == N:
            return steps, state
        
        row = len(state)
        for col in range(N):
            if is_safe(state, col):
                cost = count_attacks(state, row, col)
                new_state = state + [col]
                new_costs = costs + [cost]
                heapq.heappush(frontier, (h(new_state, new_costs), new_state, new_costs))
    
    return steps, None

def get_solution_arr():
    steps, solution = greedy_best_first_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _ = greedy_best_first_search()
    return steps

#print(get_solution_arr())