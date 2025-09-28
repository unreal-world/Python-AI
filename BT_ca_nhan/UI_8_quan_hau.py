
# Nguyễn Văn Hoài - 20110107

import Thuat_toan_DFS as thuat_toan_DFS
import Thuat_toan_BFS as thuat_toan_BFS
import Thuat_toan_UCS as thuat_toan_UCS
import Thuat_toan_DLS as thuat_toan_DLS
import Thuat_toan_IDS as thuat_toan_IDS
import Thuat_toan_Greedy_BFS as thuat_toan_Greedy
import Thuat_toan_A_star as thuat_toan_A_star
import Thuat_toan_Hill_Climbing as thuat_toan_Hill_climbing
import Thuat_toan_Beam_Search as thuat_toan_Beam_search
import Thuat_toan_Simulated_Annealing as thuat_toan_Simulated_Annealing
import Thuat_toan_Genetic_Algorithm as thuat_toan_Genetic_Algorithm
import Thuat_toan_AND_OR as thuat_toan_AND_OR
import Thuat_toan_Sensorless_Problem as thuat_toan_Sensorless_Problem

import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("8 Quan hau - Co vua")

cell_size = 60
board_size = 8 # Bàn cờ gồm 8 ô, kích thước 8x8

#-------------------------
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
    global running
    running = True
    steps, step_count, total_time = thuat_toan_BFS.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update() 
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_DFS():
    global running 
    running = True
    steps, step_count, total_time = thuat_toan_DFS.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_UCS():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_UCS.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_DLS():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_DLS.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_IDS():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_IDS.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_Greedy():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_Greedy.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_A_star():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_A_star.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update() 
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")      

def draw_board_with_Hill_climbing():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_Hill_climbing.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_Beam_search():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_Beam_search.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_Simulated_Annealing():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_Simulated_Annealing.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_Genetic_Algorithm():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_Genetic_Algorithm.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_AND_OR():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_AND_OR.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

def draw_board_with_Sensorless_Problem():
    global running
    running = True
    steps, step_count, total_time = thuat_toan_Sensorless_Problem.get_steps()
    for state in steps:
        if not running:
            break
        clear_board()
        for i in range(8):
            for j in range(8):
                if state[i][j] == 1:
                    canvas_right.create_text(
                        j * cell_size + cell_size // 2,
                        i * cell_size + cell_size // 2,
                        text="♛", font=("Arial", 32), fill="black"
                    )
        time.sleep(0.01)
        root.update()
    messagebox.showinfo("Kết quả", f"Số bước: {step_count}, Thời gian: {total_time:.4f} giây")

#---------------------------
def clear_board():
    canvas_left.delete("all")
    canvas_right.delete("all")
    draw_board()  

def stop_algorithm():
    global running
    running = False

# ----------------------
# Frame chứa 2 bàn cờ (nằm ngang)
boards_frame = tk.Frame(root)
boards_frame.pack(side=tk.TOP, pady=20)

# Frame trái
left_frame = tk.Frame(boards_frame)
left_frame.pack(side=tk.LEFT, padx=20)

# Frame phải
right_frame = tk.Frame(boards_frame)
right_frame.pack(side=tk.LEFT, padx=20)

# Canvas bên trái
canvas_left = tk.Canvas(left_frame, width=cell_size*board_size, height=cell_size*board_size)
canvas_left.pack()

# Canvas bên phải
canvas_right = tk.Canvas(right_frame, width=cell_size*board_size, height=cell_size*board_size)
canvas_right.pack()

# ----------------------
# Frame chứa các button (nằm ngang, bên dưới)
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=20)

# Danh sách button và hàm tương ứng
buttons = [
    ("Clear", clear_board),
    ("Stop", stop_algorithm),
    ("Sensorless Problem", draw_board_with_Sensorless_Problem),
    ("AND-OR", draw_board_with_AND_OR),
    ("Genetic Algorithm", draw_board_with_Genetic_Algorithm),
    ("Simulated Annealing", draw_board_with_Simulated_Annealing),
    ("Beam Search", draw_board_with_Beam_search),
    ("Hill Climbing", draw_board_with_Hill_climbing),
    ("A*", draw_board_with_A_star),
    ("Greedy", draw_board_with_Greedy),
    ("IDS", draw_board_with_IDS),
    ("DLS", draw_board_with_DLS),
    ("UCS", draw_board_with_UCS),
    ("DFS", draw_board_with_DFS),
    ("BFS", draw_board_with_BFS),
]

# Số button tối đa trên 1 hàng 
max_btn = 5

for i, (text, cmd) in enumerate(buttons):
    row = i // max_btn   # xác định dòng
    col = i % max_btn    # xác định cột
    btn = tk.Button(button_frame, text=text, font=("Arial", 12), command=cmd, width=20)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Cho các cột co giãn đều
for col in range(max_btn):
    button_frame.grid_columnconfigure(col, weight=1)
#--------------------------

draw_board()

root.mainloop()