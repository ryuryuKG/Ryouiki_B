import tkinter as tk
root = tk.Tk()
root.geometry("400x290")
canvas = tk.Canvas(root, background="#fff", width=400, height=290)
canvas.pack()
canvas.create_rectangle(30, 50, 250, 150, fill="black")
root.mainloop()