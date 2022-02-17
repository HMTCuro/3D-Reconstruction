#!/bin/bash
# Reference: https://github.com/QT-Zhu/AA-RMVSNet
python fusion_gym_color.py \
--testpath=./custom \
--testlist=./lists/custom/gym_1024_color.txt \
--outdir=./outputs_gym_800_1024_color/ \
--test_dataset=custom
