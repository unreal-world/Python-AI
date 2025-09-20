# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import random
import math

N = 8

def conflicts(state):
    # Đếm số cặp quân hậu tấn công nhau
    cnt = 0
    for c1 in range(len(state)):
        for c2 in range(c1+1, len(state)):
            if state[c1] == state[c2] or abs(state[c1]-state[c2]) == abs(c1-c2):
                cnt += 1
    return cnt

def state_to_numpy(state):
    # Chuyển state dạng list sang mảng numpy 8x8
    arr = np.zeros((N, N), dtype=int)
    for col, row in enumerate(state):
        arr[row, col] = 1
    return arr

def random_successor(state):
    # Sinh một successor ngẫu nhiên bằng cách di chuyển 1 quân hậu
    col = random.randint(0, N-1)
    row = random.randint(0, N-1)
    new_state = state.copy()
    new_state[col] = row
    return new_state

def schedule(t):
    """Hàm làm nguội: nhiệt độ giảm dần"""
    return max(0.01, min(1.0, 1.0 - 0.0001*t))

def simulated_annealing(max_iter=100000):
    # Thuật toán Simulated Annealing cho 8 quân hậu
    # Trả về (steps, solution)
    # Trạng thái ban đầu
    current = [random.randint(0, N-1) for _ in range(N)]
    steps = [state_to_numpy(current)]

    for t in range(1, max_iter+1):
        T = schedule(t)
        if T <= 0:
            break

        next_state = random_successor(current)
        deltaE = -(conflicts(next_state) - conflicts(current))  # đảo dấu để "giảm conflicts" coi như tăng VALUE

        if deltaE > 0:
            current = next_state
        else:
            if random.random() < math.exp(deltaE / T):
                current = next_state

        steps.append(state_to_numpy(current))

        # Nếu đã giải xong
        if conflicts(current) == 0:
            return steps, current

    return steps, None

def get_solution_arr():
    steps, solution = simulated_annealing()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _ = simulated_annealing()
    return steps

# print(get_solution_arr())
