#!/usr/bin/env bash
set -x
rm -Rf venv
python3 -m venv venv
./venv/bin/pip install -U pip setuptools wheel
./venv/bin/pip install -r requirements.txt
