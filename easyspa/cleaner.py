import os
import subprocess


def remove_file(file: str):
    subprocess.run(["rm", "-f", file])


def remove_directory(dirc: str):
    subprocess.run(["rm", "-rf", dirc])


def remove_grid(args):
    dirc = args.mode[1]
    grid_dirc = "mirgrid" if len(args.mode) < 3 else args.mode[2]
    join_dirc = os.path.join(dirc, grid_dirc)
    remove_directory(join_dirc)

    file = join_dirc.rstrip(os.sep) + ".pvd"
    remove_file(file)


def remove_output(args):
    dirc = args.mode[1]
    grid_dirc = "output" if len(args.mode) < 3 else args.mode[2]
    join_dirc = os.path.join(dirc, grid_dirc)
    remove_directory(join_dirc)

    file = os.path.join(dirc, "") + "log.sparta"
    remove_file(file)


def remove_build(args):
    dirc = "build" if len(args.mode) < 2 else args.mode[1]
    remove_directory(dirc)
