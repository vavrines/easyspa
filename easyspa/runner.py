import subprocess
import os

def build_sparta(args):
    dirc = "build" if len(args.mode) < 2 else args.mode[1]
    subprocess.run(["mkdir", "-p", dirc])
    os.chdir(dirc)

    subprocess.run(["cmake", "-DSPARTA_MACHINE=t", "BUILD_MPI=ON", "../sparta/cmake"])
    subprocess.run(["make", "-j", str(args.np)])
    subprocess.run(["cp", "src/spa_t", ".."])

def prepare_simulation(args):
    mode = args.mode
    dirc = mode[1]
    src = mode[2]

    subprocess.run(["cp", "-r", src, dirc])
    subprocess.run(["cp", "spa_t", dirc])
    subprocess.run(["cp", "grid2paraview.py", dirc])
    subprocess.run(["cp", "surf2paraview.py", dirc])

    print(f"Working directory: ({dirc}) setup complete")

def run_simulation(args):
    mode = args.mode
    file = mode[1]
    np = args.np

    dirc = os.path.dirname(file)
    os.chdir(dirc)
    print(f"Working directory: ({os.getcwd()})")

    local_file = os.path.basename(file)
    if np == 1:
        cmd = f"./spa_t < {local_file}"
    else:
        cmd = f"mpirun -np {np} ./spa_t < {local_file}"

    subprocess.run(cmd, shell=True)
