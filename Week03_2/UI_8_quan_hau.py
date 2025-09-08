# BT tuan 03, buoi 02 mon AI
# Nguyen Van Hoai - 20110107

import Thuat_toan_8_quan_hau as thuat_toan

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

def draw_board_with_queen():
    get_solution = thuat_toan.get_solution_arr() # Lấy nghiệm từ thuật toán
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

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)
draw_button = tk.Button(button_frame, text="Show queens", font=("Arial", 14), command=draw_board_with_queen) # Khi ấn nút sẽ show các vị trí quân hậu
draw_button.pack()

# Vẽ bàn cờ 
draw_board()

root.mainloop()