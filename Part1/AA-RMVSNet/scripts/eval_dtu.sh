#!/usr/bin/env bash

inverse_depth=False

CUDA_VISIBLE_DEVICES=0 python eval.py \
        --dataset=data_eval_transform \
        --batch_size=2 \
        --inverse_depth=${inverse_depth} \
        --numdepth=1024 \
        --interval_scale=0.2 \
        --max_h=600 \
        --max_w=800 \
        --image_scale=1.0 \
        --testpath=dtu/ \
        --testlist=lists/dtu/test2.txt \
        --loadckpt=./checkpoints/model_release.ckpt \
        --outdir=./outputs_dtu_1024
