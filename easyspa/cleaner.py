import subprocess

def remove_file(file: str):
    subprocess.run(["rm", "-f", file])

def remove_directory(dirc: str):
    subprocess.run(["rm", "-rf", dirc])
