#!/bin/bash

SEEDS="${1:-0}"
model_name="${2-electra_base_LRl-fl}"
#./../env_juwels.sh    
for task_id in "Task4" 
do
    for seed in "${SEEDS}"
    do
        python3 train.py --task_id=${task_id} --model_name=${model_name} --version="det" --seed=${seed}
    done
#    for seed in 0 1 2 3 4 5
#    do
#        python3 train.py --task_id=${task_id} --model_name=${model_name} --version="sto" --seed=${seed}
#    done
#    python3 test.py --task_id=${task_id} --model_name=${model_name}
done
