import tkinter as tk


headers = [["Exercise Filename", "Input Filename", "Output Identical?", "Time [s]"]]


def pop(res):
    window = tk.Tk()
    window.geometry("400x350")
    window.title("AbuDiffMerge - result")

    res = headers + res

    for i, row in enumerate(res):
        for j, val in enumerate(row):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            label = tk.Label(master=frame, text=str(val))
            frame.grid(row=i, column=j, sticky="news")
            label.pack()

    window.mainloop()
