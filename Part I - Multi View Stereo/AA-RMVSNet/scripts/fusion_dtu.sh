#!/bin/bash
# Reference: https://github.com/QT-Zhu/AA-RMVSNet
python fusion.py \
--testpath=dtu/ \
--testlist=./lists/dtu/test2.txt \
--outdir=./outputs_dtu/ \
--test_dataset=dtu 
