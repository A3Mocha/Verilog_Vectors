import tkinter as tk

win = tk.Tk()
win.title("Simon Says")
win.geometry("400x450")

level = 1
score = 0

txt = tk.Label(win, text="Level: 1   Score: 0", font=("Arial", 16))
txt.pack(pady=15)

status = tk.Label(win, text="waiting for fpga...", font=("Arial", 12))
status.pack(pady=5)

frame = tk.Frame(win)
frame.pack(pady=20)

# 4 squares for the buttons
up = tk.Label(frame, text="UP", bg="#226622", fg="white", width=10, height=4)
left = tk.Label(frame, text="LEFT", bg="#772222", fg="white", width=10, height=4)
right = tk.Label(frame, text="RIGHT", bg="#222277", fg="white", width=10, height=4)
down = tk.Label(frame, text="DOWN", bg="#888822", fg="white", width=10, height=4)

up.grid(row=0, column=1, padx=5, pady=5)
left.grid(row=1, column=0, padx=5, pady=5)
right.grid(row=1, column=2, padx=5, pady=5)
down.grid(row=2, column=1, padx=5, pady=5)

def reset_colors():
    up.config(bg="#226622")
    left.config(bg="#772222")
    right.config(bg="#222277")
    down.config(bg="#888822")

def handle_data(c):
    global level, score
    
    if c == 'U':
        up.config(bg="#00ff00")
        win.after(400, reset_colors)
    elif c == 'L':
        left.config(bg="#ff0000")
        win.after(400, reset_colors)
    elif c == 'R':
        right.config(bg="#0000ff")
        win.after(400, reset_colors)
    elif c == 'D':
        down.config(bg="#ffff00")
        win.after(400, reset_colors)
    elif c == 'W':
        level = level + 1
        score = score + 10
        txt.config(text="Level: " + str(level) + "   Score: " + str(score))
        status.config(text="nice! next level")
    elif c == 'X':
        level = 1
        score = 0
        txt.config(text="Level: 1   Score: 0")
        status.config(text="game over")

# fake  input using keyboard for now
def key_press(e):
    k = e.keysym
    if k == "Up":
        handle_data('U')
    elif k == "Left":
        handle_data('L')
    elif k == "Right":
        handle_data('R')
    elif k == "Down":
        handle_data('D')
    elif k == "w":
        handle_data('W')
    elif k == "x":
        handle_data('X')

win.bind("<Key>", key_press)

win.mainloop()