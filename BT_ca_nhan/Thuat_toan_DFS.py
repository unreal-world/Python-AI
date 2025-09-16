
# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np

N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        # kiểm tra đường chéo
        for d in range(1, col+1):
            if row-d >= 0 and board[row-d][col-d] == 1: return False
            if row+d < N and board[row+d][col-d] == 1: return False
    return True

def dfs():
    start = np.zeros((N, N), dtype=int)
    stack = [(start, 0)]   # (board, col)
    steps = []             # lưu tất cả các bước      

    while stack:
        board, col = stack.pop()
        steps.append(board.copy())  # lưu trạng thái hiện tại

        if col >= N:
            return steps  # đã đặt đủ 8 quân hậu

        for row in range(N):
            if is_safe(board, row, col):
                new_board = board.copy()
                new_board[row][col] = 1
                stack.append((new_board, col + 1))

    return steps

def get_solution_arr():
    #Lấy nghiệm cuối cùng (mảng numpy 8x8) từ UCS.
    steps = dfs()
    if steps:
        return steps[-1]  # trạng thái cuối cùng là nghiệm
    return None

#print(get_solution_arr())
