#!/bin/bash

# 设置环境变量
export PATH=/opt/z3-4.5.0/bin:$PATH
export LD_LIBRARY_PATH=/opt/z3-4.5.0/lib:$LD_LIBRARY_PATH

# 定义脚本列表
scripts=("tso0.rkt" "tso0-unique-simple.rkt" "tso0-simple.rkt" "tso0-unique.rkt")

# 循环运行每个脚本，并将输出重定向到对应的 .out 文件
for script in "${scripts[@]}"; do
    outfile="${script%.rkt}.out"
    racket "$script" > "$outfile"
    echo "Output of $script saved to $outfile"
done
