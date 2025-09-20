# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import random

N = 8
K = 20  # beam width 

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

def beam_search(max_iter=1000):
    """Beam Search cho 8 quân hậu"""
    beam = [[random.randint(0, N-1) for _ in range(N)] for _ in range(K)]
    steps = [state_to_numpy(s) for s in beam]

    for _ in range(max_iter):
        # Kiểm tra nghiệm
        for s in beam:
            if conflicts(s) == 0:
                return steps, s

        # Sinh neighbors
        neighbors = []
        for state in beam:
            for col in range(N):
                for row in range(N):
                    if row != state[col]:
                        new_state = state.copy()
                        new_state[col] = row
                        neighbors.append((conflicts(new_state), new_state))

        if not neighbors:
            # restart nếu không có neighbors
            beam = [[random.randint(0, N-1) for _ in range(N)] for _ in range(K)]
            steps.extend([state_to_numpy(s) for s in beam])
            continue

        # Chọn K state tốt nhất
        neighbors.sort(key=lambda x: x[0])
        beam = [s for _, s in neighbors[:K]]
        steps.extend([state_to_numpy(s) for s in beam])

    # Nếu hết max_iter mà chưa tìm thấy nghiệm
    return steps, None


def get_solution_arr():
    steps, solution = beam_search()
    if solution:
        return state_to_numpy(solution)
    return None

def get_steps():
    steps, _ = beam_search()
    return steps

#print(get_solution_arr())
