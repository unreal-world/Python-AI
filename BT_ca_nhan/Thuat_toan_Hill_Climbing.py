# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import random
import time

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
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    steps = []
    step_count = 0

    while True:
        # Khởi tạo ngẫu nhiên
        state = [random.randint(0, N-1) for _ in range(N)]
        steps.append(state_to_numpy(state))
        step_count += 1

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
            step_count += 1

            # Nếu không còn xung đột -> thành công
            if best_conflict == 0:
                total_time = time.time() - start_time
                return steps, state, step_count, total_time

        # Nếu bị kẹt nhưng chưa có nghiệm -> restart
        # tiếp tục vòng while True bên ngoài

def get_solution_arr():
    #Trả về solution dạng numpy array hoặc None
    _, solution, _, _ = hill_climbing_random_restart()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    # Trả về toàn bộ steps, step_count và total_time
    steps, _, step_count, total_time = hill_climbing_random_restart()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
