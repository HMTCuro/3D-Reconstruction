#!/bin/bash
# Reference: https://github.com/QT-Zhu/AA-RMVSNet
python fusion_dongbeiya_color.py \
--testpath=./custom \
--testlist=./lists/custom/dongbeiya_1024_color.txt \
--outdir=./outputs_dongbeiya_800_1024_color/ \
--test_dataset=custom
