#!/bin/bash
#SBATCH -J paraview0.000129
#SBATCH -N 1
#SBATCH -n  30
#SBATCH -p normal

module purge
module load compiler/rocm/dtk/22.10.1
module load compiler/devtoolset/7.3.1
module load mpi/hpcx/2.11.0/gcc-7.3.1

export PATH=$PATH:/public/home/dfzx202407/software/paraview/bin
export PATH=$PATH:/public/home/dfzx202407/software/sparta/tools/paraview

pvpython grid2paraview.py sod.txt sod_speed -r speed.1000.*
pvpython grid2paraview.py sod.txt sod_temp -r temp.1000.*
