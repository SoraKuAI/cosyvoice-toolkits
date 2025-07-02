import os
import shutil
import random

def split_data(folder_path, train_folder, val_folder, ratio=10):
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    
    wav_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".wav")])
    txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])
    
    assert len(wav_files) == len(txt_files), "WAV 和 TXT 文件数量不匹配"
    
    paired_files = list(zip(wav_files, txt_files))
    random.shuffle(paired_files)
    
    for i, (wav_file, txt_file) in enumerate(paired_files):
        target_folder = train_folder if (i % (ratio + 1)) != 0 else val_folder
        
        shutil.move(os.path.join(folder_path, wav_file), os.path.join(target_folder, wav_file))
        shutil.move(os.path.join(folder_path, txt_file), os.path.join(target_folder, txt_file))
        print(f"Moved {wav_file} and {txt_file} to {target_folder}")

# 使用示例
folder_path = "raw_audio"  # 替换为实际的文件夹路径
train_folder = os.path.join(folder_path, "train")
val_folder = os.path.join(folder_path, "val")
split_data(folder_path, train_folder, val_folder)
