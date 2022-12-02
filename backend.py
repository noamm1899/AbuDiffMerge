from prettytable import PrettyTable
import subprocess
import glob
import time
import os


def run(py_p, in_p, ex_out_p, py_out_p, debug=False):
    exs = glob.glob(os.path.join(py_p, "*.py"))
    exs_names = [os.path.splitext(os.path.basename(x))[0] for x in exs]
    test_globs = [os.path.join(in_p, f"{x}*.txt") for x in exs_names]
    test_files = [glob.glob(x) for x in test_globs]

    # tab = PrettyTable()
    # tab.field_names = ["Exercise", "Input", "Output Identical?", "Time [s]"]
    run_res = []

    for i, p_ex in enumerate(exs):
        if debug:
            print(p_ex)
        namex = os.path.basename(p_ex)
        for pi in test_files[i]:
            if debug:
                print(f"-- {pi}")
            namei = os.path.basename(pi)
            nameo = namei.replace("in", "out")
            po = fr"{py_out_p}\{nameo}"
            po_exp = fr"{ex_out_p}\{nameo}"
            runtime = 0
            if debug:
                print("--> running")
            try:
                start = time.time()
                subprocess.check_output(f"python \"{p_ex}\" < {pi} > {po}", shell=True)
                runtime = time.time() - start
                if debug:
                    print(f"--> done. {runtime}")
            except subprocess.CalledProcessError:
                if debug:
                    print("--> fail.")
                cmpres = 2
            else:
                with open(po, "rb") as f:
                    o_data = f.read().replace(b"\r", b"")
                with open(po_exp, "rb") as f:
                    o_exp_data = f.read().replace(b"\r", b"")
                cmpres = int(o_data == o_exp_data)
            cmpstr = ["FALSE", "TRUE", "ERROR"][cmpres]
            run_res.append({"ex_name": namex, "in_name": namei, "res": cmpstr, "time": round(runtime, 7)})

    return run_res
