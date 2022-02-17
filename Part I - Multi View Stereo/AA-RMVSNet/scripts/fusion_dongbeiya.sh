#!/bin/bash
# Reference: https://github.com/QT-Zhu/AA-RMVSNet
python fusion.py \
--testpath=./custom \
--testlist=./lists/custom/dongbeiya_1024.txt \
--outdir=./outputs_dongbeiya_800_1024/ \
--test_dataset=custom
