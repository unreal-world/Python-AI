
# Nguyễn Văn Hoài - 20110107

import Thuat_toan_DFS as thuat_toan_DFS
import Thuat_toan_BFS as thuat_toan_BFS
import Thuat_toan_UCS as thuat_toan_UCS
import Thuat_toan_DLS as thuat_toan_DLS
import Thuat_toan_IDS as thuat_toan_IDS
import Thuat_toan_Greedy_BFS as thuat_toan_Greedy
import Thuat_toan_A_star as thuat_toan_A_star

import tkinter as tk
import time

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
    steps = thuat_toan_BFS.bfs()
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

def draw_board_with_DFS():
    global running 
    running = True
    steps = thuat_toan_DFS.dfs()
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

def draw_board_with_UCS():
    global running
    running = True
    steps = thuat_toan_UCS.ucs()
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

def draw_board_with_DLS():
    global running
    running = True
    steps = thuat_toan_DLS.get_steps()
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

def draw_board_with_IDS():
    global running
    running = True
    steps = thuat_toan_IDS.get_steps()
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

def draw_board_with_Greedy():
    global running
    running = True
    steps = thuat_toan_Greedy.get_steps()
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

def draw_board_with_A_star():
    global running
    running = True
    steps = thuat_toan_A_star.get_steps()
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

#---------------------------
def clear_board():
    canvas_left.delete("all")
    canvas_right.delete("all")
    draw_board()  

def stop_algorithm():
    global running
    running = False

#---------------------------
button_show_bfs = tk.Frame(root)
button_show_bfs.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_bfs, text="Show queens (BFS)", font=("Arial", 14), command=draw_board_with_BFS) # Khi ấn nút sẽ show các vị trí quân hậu
draw_button.pack()

button_show_dfs = tk.Frame(root)
button_show_dfs.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_dfs, text="Show queens (DFS)", font=("Arial", 14), command=draw_board_with_DFS) 
draw_button.pack()

button_show_ucs = tk.Frame(root)
button_show_ucs.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_ucs, text="Show queens (UCS)", font=("Arial", 14), command=draw_board_with_UCS) 
draw_button.pack()

button_show_dls = tk.Frame(root)
button_show_dls.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_dls, text="Show queens (DLS)", font=("Arial", 14), command=draw_board_with_DLS) 
draw_button.pack()

button_show_ids = tk.Frame(root)
button_show_ids.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_ids, text="Show queens (IDS)", font=("Arial", 14), command=draw_board_with_IDS) 
draw_button.pack()

button_show_greedy = tk.Frame(root)
button_show_greedy.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_greedy, text="Show queens (Greedy)", font=("Arial", 14), command=draw_board_with_Greedy) 
draw_button.pack()

button_show_a_star = tk.Frame(root)
button_show_a_star.pack(side=tk.BOTTOM, pady=5)
draw_button = tk.Button(button_show_a_star, text="Show queens (A*)", font=("Arial", 14), command=draw_board_with_A_star) 
draw_button.pack()

#-----------------------------
button_stop = tk.Frame(root)
button_stop.pack(side=tk.BOTTOM, pady=5)
stop_button = tk.Button(button_stop, text="Stop", font=("Arial", 14), command=stop_algorithm)
stop_button.pack()

button_clear = tk.Frame(root)
button_clear.pack(side=tk.BOTTOM, pady=5)
clear_button = tk.Button(button_clear, text="Clear", font=("Arial", 14), command=clear_board)
clear_button.pack()

draw_board()

root.mainloop()