# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(board, row, col):
    # Kiểm tra xem có thể đặt quân hậu ở (row, col) không
    for i in range(col):
        if board[row][i] == 1:
            return False
        # kiểm tra đường chéo
        for d in range(1, col+1):
            if row-d >= 0 and board[row-d][col-d] == 1:
                return False
            if row+d < N and board[row+d][col-d] == 1:
                return False
    return True

def goal_test(board, col):
    return col >= N

class NQueenProblem:
    def __init__(self, N):
        self.N = N
        self.initial = (np.zeros((N, N), dtype=int), 0)  # (board, col)

    def actions(self, state):
        board, col = state
        if col >= self.N:
            return []
        acts = []
        for row in range(self.N):
            if is_safe(board, row, col):
                acts.append(row)   # hành động = đặt quân hậu ở hàng 'row'
        return acts

    def results(self, state, action):
        board, col = state
        new_board = board.copy()
        new_board[action][col] = 1
        return [(new_board, col+1)]  # kết quả là 1 trạng thái duy nhất

    def goal_test(self, state):
        board, col = state
        return goal_test(board, col)

# DFS AND-OR SEARCH
def state_to_key(state):
    board, col = state
    return (tuple(map(tuple, board)), col)

def And_Or_Graph_Search(problem):
    # DFS AND-OR search
    return Or_Search(problem.initial, problem, set(), [])

def Or_Search(state, problem, path, steps):
    board, col = state
    steps.append(board.copy())

    if problem.goal_test(state):
        return [], steps  # empty plan

    if state_to_key(state) in path:
        return None, steps  # failure (vòng lặp)

    new_path = set(path)
    new_path.add(state_to_key(state))

    # DFS: duyệt tuần tự từng action
    for action in problem.actions(state):
        result_states = problem.results(state, action)
        plan, steps = And_Search(result_states, problem, new_path, steps)
        if plan is not None:  # thành công thì trả về ngay
            return [(action, plan)], steps

    return None, steps  # thất bại nếu thử hết action mà không thành công

def And_Search(states, problem, path, steps):
    plans = []
    for s in states:
        plan, steps = Or_Search(s, problem, path, steps)
        if plan is None:
            return None, steps
        plans.append(plan)
    return plans, steps

def run_and_or():
    start_time = time.time()
    problem = NQueenProblem(N)
    plan, steps = And_Or_Graph_Search(problem)
    total_time = time.time() - start_time

    solution = None
    if steps:
        last_board = steps[-1]
        if goal_test(last_board, N):
            solution = last_board

    return steps, solution, len(steps), total_time


def get_solution_arr():
    # Lấy nghiệm cuối cùng (numpy array 8x8) hoặc None
    _, solution, _, _ = run_and_or()
    return solution

def get_steps():
    # Lấy tất cả steps, step_count, và thời gian
    steps, _, step_count, total_time = run_and_or()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
