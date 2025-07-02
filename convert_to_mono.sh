#!/bin/bash

# 遍历当前目录下所有 .wav 文件
for file in *.wav; do
    if [ -f "$file" ]; then
        echo "正在处理: $file"
        
        # 使用 ffmpeg 将音频转换为单声道（覆盖原文件）
        ffmpeg -y -i "$file" -ac 1 -loglevel error -stats "tmp_$file"
        
        # 如果转换成功，就替换原文件
        if [ -f "tmp_$file" ]; then
            mv "tmp_$file" "$file"
            echo "已转换为单声道: $file"
        else
            echo "转换失败: $file"
        fi
    fi
done

