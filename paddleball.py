from tkinter import*
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        canvas.move(self.id, 245, 100)

    def draw(self):
        self.canvas.move(self.id, 0, -1)


tk = Tk()
tk.title('Game')  # title displayed in game window
tk.resizable(0, 0)  # make sure size of window cannot be changed
# place window with canvas in front of all others
tk.wm_attributes('-topmost', 1)
# make sure there is no border
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()  # tkinter will initialize for animation

ball = Ball(canvas, 'Red')

# animation(main) loop - tkinter keeps redrawing screen
while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
