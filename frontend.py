from tkinter import filedialog as fd
import tkinter as tk
import os.path
import backend
import fe_res


def set_error(msg):
    error_tx.config(state=tk.NORMAL)
    error_tx.delete("1.0", tk.END)
    error_tx.insert("1.0", msg)
    error_tx.config(state=tk.DISABLED)


def press_run():
    # Get paths
    py_p = py_path_en.get()
    in_p = in_path_en.get()
    ex_out_p = ex_out_path_en.get()
    py_out_p = py_out_path_en.get()

    # Check Input
    if not os.path.isdir(py_p):
        set_error(f"{py_p} is not an existing directory")
        return
    if not os.path.isdir(in_p):
        set_error(f"{in_p} is not an existing directory")
        return
    if not os.path.isdir(ex_out_p):
        set_error(f"{ex_out_p} is not an existing directory")
        return
    if not os.path.isdir(py_out_p):
        set_error(f"{py_out_p} is not an existing directory")
        return

    res = backend.run(py_p, in_p, ex_out_p, py_out_p)
    fe_res.pop(res)


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
execute_bn = tk.Button(master=execute_fr, text="Run!", width=12, command=press_run)

error_fr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
error_tx = tk.Text(master=error_fr, state=tk.DISABLED, fg="red", width=61, height=5)

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

# Insert Default Values
#######################
py_path_en.insert(0, "exercise files")
in_path_en.insert(0, r"tests\input")
ex_out_path_en.insert(0, r"tests\output")
py_out_path_en.insert(0, "my_output")

# Run
#####
window.mainloop()
