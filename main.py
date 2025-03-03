import tkinter as tk

class CircleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Два круга")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        # Рисуем два круга
        self.draw_circles()

    def draw_circles(self):
        # Первый круг
        self.canvas.create_oval(50, 50, 150, 150, fill='blue', outline='black')
        # Второй круг
        self.canvas.create_oval(250, 50, 350, 150, fill='red', outline='black')

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
