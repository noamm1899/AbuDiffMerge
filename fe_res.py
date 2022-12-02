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

            if i == 0:
                frame.config(bg="gray")
                label.config(font="default 9 bold")
            elif j == 2:
                bg_col = ["red", "yellow", "green"][int(val != "ERROR") + int(val == "TRUE")]
                fg_col = ["white", "black", "white"][int(val != "ERROR") + int(val == "TRUE")]
                label.config(fg=fg_col, bg=bg_col)
                frame.config(bg=bg_col)
            elif j == 3:
                bg_col = ["red", "green"][float(val) < 5]
                fg_col = "white"
                label.config(fg=fg_col, bg=bg_col)
                frame.config(bg=bg_col)
            frame.grid(row=i, column=j, sticky="news")
            label.pack()

    window.mainloop()
