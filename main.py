import argparse
import os
import subprocess

from easyspa import remove_file, remove_directory


def parse_arguments():
    """
    Parse command-line arguments
    
    Returns:
        Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(prog = "easyspa", description='To make life easier with sparta.')
    
    parser.add_argument(
        "mode",
        nargs="+",
        help="execution mode"
    )

    parser.add_argument(
        '-i', '--input', 
        type=str, 
        #required=True, 
        help="Path to the input file."
    )
    parser.add_argument(
        "-np",
        default=1,
        type=int,
        help="number of processors"
    )
    
    args = parser.parse_args()
    return args


def select_mode(mode):
    match mode[0]:
        case "run":
            return run_simulation
        case "build":
            return build_sparta
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


def run_simulation(args):
    mode = args.mode
    file = mode[1]
    np = args.np
    
    if np == 1:
        cmd = f"./spa_t < {file}"
    else:
        cmd = f"mpirun -np {np} spa_t < {file}"

    subprocess.run(cmd, shell=True)


def build_sparta(args):
    '''Build sparta binary'''
    subprocess.run(["mkdir", "-p", "build"])
    os.chdir("build/")
    subprocess.run(["cmake", "-DSPARTA_MACHINE=t", "BUILD_MPI=ON", "../sparta/cmake"])
    subprocess.run(["make", "-j", str(args.np)])


def clean_build(args):
    '''Clean sparta build'''
    remove_directory("build")


def main():
    args = parse_arguments()
    adict = args.__dict__
    fn = select_mode(args.mode)
    fn(args)


if __name__ == "__main__":
    main()
