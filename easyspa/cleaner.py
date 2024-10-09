import subprocess

def remove_file(file: str):
    subprocess.run(["rm", "-f", file])

def remove_directory(dirc: str):
    subprocess.run(["rm", "-rf", dirc])

def remove_grid(args):
    dirc = args.mode[1]
    file = dirc + ".pvd"
    remove_file(file)
    remove_directory(dirc)

def remove_output(args):
    dirc = args.mode[1]
    remove_directory(dirc)
    file = f"{dirc}/../" + "log.sparta"
    remove_file(file)

def remove_build(args):
    dirc = "build" if len(args.mode)<2 else args.mode[1]
    remove_directory(dirc)
