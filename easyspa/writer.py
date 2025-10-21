import os
import subprocess

def write_solution(args):
    mode = args.mode
    x = args.x

    dirc = "run/" if len(mode) < 2 else mode[1]
    os.chdir(dirc)
    print(f"Working directory: ({os.getcwd()})")

    grid = "mir.txt" if len(mode) < 3 else mode[2]
    src = "output/" if len(mode) < 4 else mode[3]
    dirc = "mirgrid" if len(mode) < 5 else mode[4]

    subprocess.run(["pvpython", "grid2paraview.py", grid, dirc, "-r", f"{src}/grid.*", "-x", str(x)])
