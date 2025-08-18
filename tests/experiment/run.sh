#!/bin/bash

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../" && pwd)"
export PYTHONPATH="$ROOT_DIR:$PYTHONPATH"

python3 ./exp1_inject_test.py
python3 ./exp1_statistic_litmus_trans.py
python3 ./exp2_synth_test.py
python3 ./exp2_synth_rvtso.py
python3 ./exp2_synth_rvtso_align_memsynth.py
python3 ./exp3_chip_test.py
python3 ./exp3_chip_test_U740.py
python3 ./exp3_qemu_test.py
python3 ./exp4_cycle_test_C910.py
python3 ./exp4_cycle_test_rvwmo.py
python3 ./exp4_cycle_test_TSO.py
python3 ./exp5_other_model.py
python3 ./exp5_img.py