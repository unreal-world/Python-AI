# Nguồn: Tham khảo từ AI
# Nguyễn Văn Hoài - 20110107

import numpy as np
import time

N = 8

def is_safe(row, col, queens):
    # Kiểm tra (row, col) có an toàn không so với các quân hậu đã đặt.
    # queens: dict {row: col}

    for r, c in queens.items():
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def forward_check(domains, row, col):
    # Cập nhật miền giá trị (domains) sau khi đặt hậu tại (row, col).
    # Trả về bản sao miền mới hoặc None nếu bị cắt (không còn giá trị nào).

    new_domains = {r: set(cols) for r, cols in domains.items()}
    for r in range(row + 1, N):
        if col in new_domains[r]:
            new_domains[r].remove(col)           # cùng cột
        diag_left = col - (r - row)
        diag_right = col + (r - row)
        if diag_left in new_domains[r]:
            new_domains[r].remove(diag_left)     # chéo trái
        if diag_right in new_domains[r]:
            new_domains[r].remove(diag_right)    # chéo phải
        if not new_domains[r]:                   # không còn giá trị nào
            return None
    return new_domains

def backtrack_fc(queens, domains, row, steps, step_counter):
    step_counter[0] += 1

    if row == N:
        return True  # đã gán đủ biến

    for col in list(domains[row]):
        if is_safe(row, col, queens):
            queens[row] = col
            new_domains = forward_check(domains, row, col)
            board = np.zeros((N, N), dtype=int)
            for r, c in queens.items():
                board[r, c] = 1
            steps.append(board)

            if new_domains is not None:
                if backtrack_fc(queens, new_domains, row + 1, steps, step_counter):
                    return True

            # Quay lui
            del queens[row]

    return False

def solve_forward_checking():
    start_time = time.time()
    steps = []
    step_counter = [0]

    # Khởi tạo miền giá trị: mỗi hàng có thể chọn bất kỳ cột nào
    domains = {r: set(range(N)) for r in range(N)}
    queens = {}

    success = backtrack_fc(queens, domains, 0, steps, step_counter)

    total_time = time.time() - start_time
    if success:
        board = np.zeros((N, N), dtype=int)
        for r, c in queens.items():
            board[r, c] = 1
        return steps, board, step_counter[0], total_time
    else:
        return steps, None, step_counter[0], total_time

def get_solution_arr():
    _, solution, _, _ = solve_forward_checking()
    return solution

def get_steps():
    steps, _, step_count, total_time = solve_forward_checking()
    return steps, step_count, total_time

if __name__ == "__main__":
    sol = get_solution_arr()
    print("Solution:\n", sol)
    steps, step_count, total_time = get_steps()
    print("Số bước chạy:", step_count)
    print("Thời gian chạy: %.4f giây" % total_time)
