import os
import shutil

def convert_speaker_list_to_lab(speaker_list_file):
    with open(speaker_list_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 4:
                file_path = parts[0]
                text = parts[3]
                file_name = os.path.splitext(os.path.basename(file_path))[0]
                lab_file = f"{file_name}.normalized.txt"
                with open(lab_file, 'w', encoding='utf-8') as lab:
                    lab.write(text)
                    print(f"Generated {lab_file}")
                shutil.move(lab_file, os.path.join("raw_audio", lab_file))


convert_speaker_list_to_lab("speaker_jp.list")
print("转换完成")

