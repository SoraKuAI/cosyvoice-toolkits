#!/bin/bash

# 提取 speaker.list 中的文件名
awk -F "|" '{print $1}' speaker_jp.list | awk -F "/" '{print $3}' > valid_files.txt

# 遍历 raw_audio 目录中的文件
for file in raw_audio/*.wav; do
    filename=$(basename "$file")
    # 检查文件是否在 valid_files.txt 中
    if ! grep -q "^$filename$" valid_files.txt; then
        echo "删除: $file"
        rm "$file"
    fi
done

# 清理临时文件
rm valid_files.txt

