# BT tuan 04, buoi 01 mon AI
# Nguyen Van Hoai - 20110107

import Thuat_toan_DFS as thuat_toan_DFS
import Thuat_toan_BFS as thuat_toan_BFS

import tkinter as tk

root = tk.Tk()
root.title("8 Quan hau - Co vua")

cell_size = 60
board_size = 8 # Bàn cờ gồm 8 ô, kích thước 8x8

# Tạo hai frame bên trái và phải
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=50, pady=50)
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=50, pady=50)

# Canvas bên trái
canvas_left = tk.Canvas(left_frame, width=cell_size*board_size, height=cell_size*board_size)
canvas_left.pack()

# Canvas bên phải
canvas_right = tk.Canvas(right_frame, width=cell_size*board_size, height=cell_size*board_size)
canvas_right.pack()

def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas_left.create_rectangle(x1, y1, x2, y2, fill=color)
            canvas_right.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_board_with_BFS():
    get_solution = thuat_toan_BFS.get_solution_arr() # Lấy nghiệm từ thuật toán
    arr_x = [] # Mảng lưu vị trí các quân hậu
    arr_y = [0, 1, 2, 3, 4, 5, 6, 7] # Vị trí cố định
    for i in range(8):
        for j in range(8):
            if get_solution[i][j] == 1:
                arr_x.append(j)
    for i in range(8):
        canvas_right.create_text(
            arr_x[i] * cell_size + cell_size // 2,
            arr_y[i] * cell_size + cell_size // 2,
            text="♛", font=("Arial", 32), fill="black"
        )

def draw_board_with_DFS():
    get_solution = thuat_toan_DFS.get_solution_arr() # Lấy nghiệm từ thuật toán
    arr_x = [] # Mảng lưu vị trí các quân hậu
    arr_y = [0, 1, 2, 3, 4, 5, 6, 7] # Vị trí cố định
    for i in range(8):
        for j in range(8):
            if get_solution[i][j] == 1:
                arr_x.append(j)
    for i in range(8):
        canvas_right.create_text(
            arr_x[i] * cell_size + cell_size // 2,
            arr_y[i] * cell_size + cell_size // 2,
            text="♛", font=("Arial", 32), fill="black"
        )

def clear_board():
    canvas_left.delete("all")
    canvas_right.delete("all")
    draw_board()  # Vẽ lại bàn cờ trống

button_show_bfs = tk.Frame(root)
button_show_bfs.pack(side=tk.BOTTOM, pady=20)
draw_button = tk.Button(button_show_bfs, text="Show queens (BFS)", font=("Arial", 14), command=draw_board_with_BFS) # Khi ấn nút sẽ show các vị trí quân hậu
draw_button.pack()

button_show_dfs = tk.Frame(root)
button_show_dfs.pack(side=tk.BOTTOM, pady=20)
draw_button = tk.Button(button_show_dfs, text="Show queens (DFS)", font=("Arial", 14), command=draw_board_with_DFS) # Khi ấn nút sẽ show các vị trí quân hậu
draw_button.pack()

button_clear = tk.Frame(root)
button_clear.pack(side=tk.BOTTOM, pady=20)
clear_button = tk.Button(button_clear, text="Clear", font=("Arial", 14), command=clear_board)
clear_button.pack()

# Vẽ bàn cờ 
draw_board()

root.mainloop()