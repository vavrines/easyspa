#!/bin/bash
#SBATCH -J sod_Kn0.000129
#SBATCH -N 1
#SBATCH -n 30
#SBATCH -p normal

module purge
module load compiler/rocm/dtk/22.10.1
module load compiler/devtoolset/7.3.1
module load mpi/hpcx/2.11.0/gcc-7.3.1

export PATH=$PATH:/public/home/dfzx202407/software/sparta/build/src

mpirun -np 30 spa_tutorial < in.sod
