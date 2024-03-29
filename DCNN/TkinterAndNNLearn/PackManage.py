import tkinter as tk

window = tk.Tk()

"""
frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)
"""

"""
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.RIGHT)
"""

frame1 = tk.Frame(master=window, width=100, bg="white")
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="red")
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame3 = tk.Frame(master=window, width=100, bg="white")
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

window.mainloop()
