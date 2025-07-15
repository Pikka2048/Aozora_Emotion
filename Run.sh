#!/bin/bash
python3 -m venv venv

# GPUがない場合: venv/bin/python -m pip install -r requestment_cpu.txt
venv/bin/python -m pip install -r requestment.txt

# 件数制限する場合: venv/bin/python aozora_emotion.py --n 5
venv/bin/python aozora_emotion.py
venv/bin/python plot_glob.py