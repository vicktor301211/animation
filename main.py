import random
import time
import tkinter as tk
from tkinter import PhotoImage


# Родительский класс
class AnimatedObject:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

# Класс-наследник
class Ball(AnimatedObject):
    def __init__(self, canvas, radius, color="yellow",):
        x = random.randint(radius, canvas.winfo_reqwidth() - radius)
        y = random.randint(radius, canvas.winfo_reqheight() - radius)
        super().__init__(canvas, x, y)
        self.radius = radius
        self.color = color
        self.id = canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=self.color
        )

    def draw(self):
        pass

# Основная программа
root = tk.Tk()
root.title('Анимация "Пчела"')

width = 1600
height = 900
canvas = tk.Canvas(root, width=width, height=height, bg = 'lightblue')
canvas.pack()

# Ждем пока canvas появится на экране
root.update_idletasks()

# Теперь создаем шар
lug = PhotoImage(file='lug.png')
lug_id = canvas.create_image(0, 600, anchor = 'center', image = lug)
ball = Ball(canvas, 30)
while True:
    ball.move(random.randint(-10, 10), random.randint(-10, 10))
    root.update()
    time.sleep(0.05)

root.mainloop()

