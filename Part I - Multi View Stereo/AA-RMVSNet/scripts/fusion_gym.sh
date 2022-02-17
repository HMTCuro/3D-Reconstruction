#!/bin/bash
# Reference: https://github.com/QT-Zhu/AA-RMVSNet
python fusion.py \
--testpath=./custom \
--testlist=./lists/custom/gym_1024.txt \
--outdir=./outputs_gym_800_1024/ \
--test_dataset=custom
