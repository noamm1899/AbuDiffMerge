from prettytable import PrettyTable
import subprocess
import glob
import time
import os

DEBUG = False

exs = glob.glob(r"exercise files\*.py")
exs_names = [os.path.splitext(os.path.basename(x))[0] for x in exs]
test_globs = [fr"tests\input\{x}*.txt" for x in exs_names]
test_files = [glob.glob(x) for x in test_globs]

tab = PrettyTable()
tab.field_names = ["Exercise", "Input", "Output Identical?", "Time [s]"]

for i, p_ex in enumerate(exs):
    if DEBUG:
        print(p_ex)
    namex = os.path.basename(p_ex)
    for pi in test_files[i]:
        if DEBUG:
            print(f"-- {pi}")
        namei = os.path.basename(pi)
        nameo = namei.replace("in", "out")
        po = fr"my_output\{nameo}"
        po_exp = fr"tests\output\{nameo}"
        runtime = 0
        if DEBUG:
            print("--> running")
        try:
            start = time.time()
            res = subprocess.check_output(f"python \"{p_ex}\" < {pi} > {po}", shell=True)
            runtime = time.time() - start
            if DEBUG:
                print(f"--> done. {runtime}")
        except subprocess.CalledProcessError:
            if DEBUG:
                print("--> fail.")
            cmpres = 2
        else:
            with open(po, "rb") as f:
                o_data = f.read().replace(b"\r", b"")
            with open(po_exp, "rb") as f:
                o_exp_data = f.read().replace(b"\r", b"")
            cmpres = int(o_data == o_exp_data)
        cmpstr = [f"\033[93m\033[1mFALSE\033[0m", f"\033[92m\033[1mTRUE\033[0m", f"\033[91m\033[1mERROR\033[0m"][cmpres]
        tab.add_row([namex, namei, cmpstr, round(runtime, 7)])

print(tab)