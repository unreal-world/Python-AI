# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import random
import math
import time

N = 8

def conflicts(state):
    # Tính số cặp quân hậu tấn công nhau trong state
    cnt = 0
    for r1 in range(N):
        for r2 in range(r1+1, N):
            c1, c2 = state[r1], state[r2]
            if c1 == c2 or abs(c1 - c2) == abs(r1 - r2):
                cnt += 1
    return cnt

def random_neighbor(state):
    # Sinh hàng xóm bằng cách đổi cột của 1 quân hậu
    neighbor = state.copy()
    row = random.randint(0, N-1)
    new_col = random.randint(0, N-1)
    while new_col == neighbor[row]:
        new_col = random.randint(0, N-1)
    neighbor[row] = new_col
    return neighbor

def state_to_numpy(state):
    # Chuyển state (list cột theo từng hàng) sang mảng 8x8
    arr = np.zeros((N, N), dtype=int)
    for row, col in enumerate(state):
        arr[row, col] = 1
    return arr

def simulated_annealing(max_steps=10000, T_start=100.0, cooling=0.99):
    # Simulated Annealing cho 8 quân hậu
    # Trả về (steps, solution, step_count, elapsed_time):
    #  - steps: danh sách các board (numpy 8x8) theo thứ tự xét
    #  - solution: state cuối cùng nếu tìm thấy
    #  - step_count: số bước đã chạy
    #  - elapsed_time: thời gian chạy (giây)

    start_time = time.time()

    # Khởi tạo ngẫu nhiên
    state = [random.randint(0, N-1) for _ in range(N)]
    steps = [state_to_numpy(state)]
    cost = conflicts(state)
    T = T_start

    for step in range(max_steps):
        if cost == 0:
            elapsed = time.time() - start_time
            return steps, state, step+1, elapsed  # nghiệm hợp lệ

        neighbor = random_neighbor(state)
        new_cost = conflicts(neighbor)

        delta = new_cost - cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            # chấp nhận state mới
            state = neighbor
            cost = new_cost
            steps.append(state_to_numpy(state))

        T *= cooling  # giảm nhiệt độ

    elapsed = time.time() - start_time
    return steps, None, max_steps, elapsed  # hết vòng lặp mà chưa tìm thấy

def get_solution_arr():
    _, solution, _, _ = simulated_annealing()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _, step_count, total_time = simulated_annealing()
    return steps, step_count, total_time


if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
