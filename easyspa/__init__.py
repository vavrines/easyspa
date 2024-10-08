"""
Make life easier with sparta
==================================

DSMC suite for particle transport
Copyright (c) 2024 Tianbai Xiao <tianbaixiao@gmail.com>
"""

import easyspa.parser
import easyspa.runner
import easyspa.writer
import easyspa.cleaner

from easyspa.parser import *
from easyspa.runner import *
from easyspa.writer import *
from easyspa.cleaner import *

from easyspa.__about__ import __author__, __author_email__, __version__

def select_mode(mode):
    match mode[0]:
        case "build":
            return build_sparta
        case "prepare":
            return prepare_simulation
        case "run":
            return run_simulation
        case "paraview":
            return write_solution
        case "rmgrid":
            return remove_grid
        case "rmout":
            return remove_output
        case "unmake":
            return remove_build
        case _:
            return "Something's wrong with the internet"
