from tkinter import filedialog as fd
import tkinter as tk

# Initialize window
###################
window = tk.Tk()
window.geometry("500x200")
window.title("AbuDiffMerge")

# Define components
###################
py_path_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
py_path_lb = tk.Label(master=py_path_fr, text="Python Files Path")
py_path_en = tk.Entry(master=py_path_fr, width=58)
# py_path_bn = tk.Button(master=py_path_fr, text="Select Path")

in_path_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
in_path_lb = tk.Label(master=in_path_fr, text="Input Files Path")
in_path_en = tk.Entry(master=in_path_fr, width=58)
# in_path_bn = tk.Button(master=in_path_fr, text="Select Path")

ex_out_path_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
ex_out_path_lb = tk.Label(master=ex_out_path_fr, text="Example Output Files Path")
ex_out_path_en = tk.Entry(master=ex_out_path_fr, width=58)
# ex_out_path_bn = tk.Button(master=ex_out_path_fr, text="Select Path")

py_out_path_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
py_out_path_lb = tk.Label(master=py_out_path_fr, text="Python Output Files Path")
py_out_path_en = tk.Entry(master=py_out_path_fr, width=58)
# py_out_path_bn = tk.Button(master=py_out_path_fr, text="Select Path")

execute_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
execute_bn = tk.Button(master=execute_fr, text="Run!", width=12)

error_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
error_tx = tk.Text(master=error_fr, state=tk.DISABLED, fg="red", width=61)

# Place components
##################
py_path_fr.grid(row=0, column=0, sticky="ew")
py_path_lb.pack(side=tk.LEFT)
py_path_en.pack(side=tk.RIGHT)
# py_path_bn.pack()

in_path_fr.grid(row=1, column=0, sticky="ew")
in_path_lb.pack(side=tk.LEFT)
in_path_en.pack(side=tk.RIGHT)
# in_path_bn.pack()

ex_out_path_fr.grid(row=2, column=0, sticky="ew")
ex_out_path_lb.pack(side=tk.LEFT)
ex_out_path_en.pack(side=tk.RIGHT)
# ex_out_path_bn.pack()

py_out_path_fr.grid(row=3, column=0, sticky="ew")
py_out_path_lb.pack(side=tk.LEFT)
py_out_path_en.pack(side=tk.RIGHT)
# py_out_path_bn.pack()

execute_fr.grid(row=4, column=0, sticky="ew")
execute_bn.pack(side=tk.RIGHT)

error_fr.grid(row=5, column=0, sticky="ew")
error_tx.pack()

# Run
#####
window.mainloop()
