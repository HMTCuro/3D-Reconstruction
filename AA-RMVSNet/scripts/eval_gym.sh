#!/usr/bin/env bash

inverse_depth=False

CUDA_VISIBLE_DEVICES=0 python eval.py \
        --dataset=custom \
        --batch_size=1 \
        --inverse_depth=${inverse_depth} \
        --numdepth=512 \
        --interval_scale=0.4 \
        --max_h=600 \
        --max_w=800 \
        --image_scale=1.0 \
        --testpath=custom/ \
        --testlist=lists/custom/gym.txt \
        --loadckpt=./checkpoints/model_000002.ckpt \
        --outdir=./outputs_gym
