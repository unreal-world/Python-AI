# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import random

N = 8

def conflicts(state):
    # Đếm số cặp quân hậu tấn công nhau trong state
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

def hill_climbing_random_restart():
    # Thuật toán Hill-Climbing với Random Restart cho 8 quân hậu
    # Trả về (steps, solution):
    #   - steps: danh sách numpy 8x8 các bước
    #   - solution: state cuối cùng chắc chắn là nghiệm
    steps = []

    while True:
        # Khởi tạo ngẫu nhiên
        state = [random.randint(0, N-1) for _ in range(N)]
        steps.append(state_to_numpy(state))

        while True:
            current_conflicts = conflicts(state)
            neighbors = []

            # Sinh neighbors bằng cách di chuyển 1 quân hậu trong 1 cột sang hàng khác
            for col in range(N):
                for row in range(N):
                    if row != state[col]:
                        new_state = state.copy()
                        new_state[col] = row
                        neighbors.append((conflicts(new_state), new_state))

            # Tìm neighbor tốt nhất
            best_conflict, best_state = min(neighbors, key=lambda x: x[0])

            # Nếu không có neighbor tốt hơn -> kẹt
            if best_conflict >= current_conflicts:
                break

            # Chuyển sang neighbor tốt hơn
            state = best_state
            steps.append(state_to_numpy(state))

            # Nếu không còn xung đột -> thành công
            if best_conflict == 0:
                return steps, state

        # Nếu bị kẹt nhưng chưa có nghiệm -> restart
        # tiếp tục vòng while True bên ngoài

def get_solution_arr():
    steps, solution = hill_climbing_random_restart()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _ = hill_climbing_random_restart()
    return steps

# print(get_solution_arr())
