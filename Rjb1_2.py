import tkinter as tk
root = tk.Tk()
root.geometry("400x290")
canvas = tk.Canvas(root, background="#fff", width=400, height=290)
canvas.pack()
canvas.create_rectangle(80,20,150, 100, fill="black")
canvas.create_rectangle(30, 50, 200, 100, fill="black")
canvas.create_oval(50, 100, 80, 130, fill="black")
canvas.create_oval(150, 100, 180, 130, fill="black")
message = tk.Label(text="Ito Ryuta",background="#fff",font=("MSゴシック","15","bold"))
message.place(x=70,y=150)
root.mainloop()