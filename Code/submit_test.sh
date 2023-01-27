#!/bin/bash -x
#SBATCH --account=deepacf
#SBATCH --nodes=1
#SBATCH --output=gpu-out.%j
#SBATCH --error=gpu-err.%j
#SBATCH --time=24:00:00
#SBATCH --partition=booster
#SBATCH --gres=gpu:4

export FOLDER_UQPLM_DATA="/p/scratch/deepacf/maelstrom/maelstrom_data/ap2/data/UQ-PLM/"
module purge
module load Stages/2023
module load cuDNN/8.6.0.163-CUDA-11.7
module load GCC/11.3.0
module load Emacs/28.2
module unload Python/3.10.4
conda activate uq-plm
module list

srun --exclusive -n 1 --gres=gpu:1 --cpu-bind=map_cpu:0  ./run_juwels.sh 0 &
srun --exclusive -n 1 --gres=gpu:1 --cpu-bind=map_cpu:10 ./run_juwels.sh 1 &
srun --exclusive -n 1 --gres=gpu:1 --cpu-bind=map_cpu:20 ./run_juwels.sh 2 &
srun --exclusive -n 1 --gres=gpu:1 --cpu-bind=map_cpu:30 ./run_juwels.sh 3 &

wait
