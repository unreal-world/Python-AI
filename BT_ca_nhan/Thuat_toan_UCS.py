# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import heapq
import itertools
import time

N = 8
counter = itertools.count()  # bộ đếm duy nhất để tránh so sánh numpy

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        for d in range(1, col+1):
            if row-d >= 0 and board[row-d][col-d] == 1:
                return False
            if row+d < N and board[row+d][col-d] == 1:
                return False
    return True

def cost_of_placement(board, row, col):
    #Tính chi phí khi đặt một quân hậu tại (row, col):
    # Các ô bên phải cùng hàng
    # Các ô trên 2 đường chéo bên phải

    count = 0
    for j in range(col+1, N):  # cùng hàng bên phải
        count += 1
    for d in range(1, N):      # các đường chéo bên phải
        if row-d >= 0 and col+d < N:
            count += 1
        if row+d < N and col+d < N:
            count += 1
    return count

def ucs():
    # Uniform Cost Search cho 8 quân hậu.
    # Trả về (steps, solution, step_count, total_time)

    start_time = time.time()
    step_count = 0

    start = np.zeros((N, N), dtype=int)
    pq = [(0, next(counter), start, 0)]  # (cost, id, board, col)
    steps = []

    while pq:
        cost, _, board, col = heapq.heappop(pq)
        steps.append(board.copy())
        step_count += 1

        if col >= N:
            total_time = time.time() - start_time
            return steps, board, step_count, total_time  # nghiệm chi phí nhỏ nhất

        for row in range(N):
            if is_safe(board, row, col):
                new_board = board.copy()
                new_board[row][col] = 1
                new_cost = cost + cost_of_placement(board, row, col)
                heapq.heappush(pq, (new_cost, next(counter), new_board, col + 1))

    total_time = time.time() - start_time
    return steps, None, step_count, total_time

def get_solution_arr():
    # Lấy nghiệm cuối cùng (numpy array 8x8) hoặc None
    _, solution, _, _ = ucs()
    return solution

def get_steps():
    # Lấy tất cả steps, step_count và thời gian
    steps, _, step_count, total_time = ucs()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
