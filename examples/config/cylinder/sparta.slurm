#!/bin/bash
#SBATCH -J sparta
#SBATCH -N 1
#SBATCH --ntasks-per-node 64
#SBATCH -p hfacnormal02

mpirun -np 64 ./spa_t < ma2cylinder.cfg
