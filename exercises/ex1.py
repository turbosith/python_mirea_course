import tkinter as tk

label = tk.Label()
label = tk.Canvas(width=700, height=700, bg="black")
label.create_oval([70, 70], [500, 500], fill="yellow")
label.create_oval([300, 100], [400, 200], fill="black")
label.create_polygon([300, 300], [500, 500], [500, 100], fill="black")
label.pack()
tk.mainloop()