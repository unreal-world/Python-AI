
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import heapq
import itertools

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
    #Chiếm bao nhiêu ô bên phải cùng hàng + 2 đường chéo bên phải

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
    #Trả về tất cả các bước (steps) để thuật toán UCS tìm nghiệm.

    start = np.zeros((N, N), dtype=int)
    pq = [(0, next(counter), start, 0)]  # (cost, id, board, col)
    steps = []

    while pq:
        cost, _, board, col = heapq.heappop(pq)
        steps.append(board.copy())

        if col >= N:
            return steps  # nghiệm chi phí nhỏ nhất

        for row in range(N):
            if is_safe(board, row, col):
                new_board = board.copy()
                new_board[row][col] = 1
                new_cost = cost + cost_of_placement(board, row, col)
                heapq.heappush(pq, (new_cost, next(counter), new_board, col + 1))

    return steps

def get_solution_arr():
    #Lấy nghiệm cuối cùng (mảng numpy 8x8) từ UCS.
    steps = ucs()
    if steps:
        return steps[-1]  # trạng thái cuối cùng là nghiệm
    return None

#print(get_solution_arr())
