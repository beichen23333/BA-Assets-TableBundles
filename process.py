import json
import os
import zipfile
from pathlib import Path

# 定义仓库路径
repo1_path = Path(".")
repo2_path = Path("BA-Text")

# 创建临时文件夹
temp_path = Path("temp")
temp_path.mkdir(exist_ok=True)

# 加载load.json文件
load_file = repo1_path / "load.json"
with open(load_file, 'r', encoding='utf-8') as f:
    load_data = json.load(f)

# 比较文件并处理
def compare_and_process(file1_path, file2_path, output_path compare,_key):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1:
            file1_data = json.load(file1)
        with open(file2_path, 'r', encoding='utf-8') as file2:
            file2_data = json.load(file2)
        
        # 获取文件1中所有的键值
        file1_keys = {item[compare_key] for item in file1_data if compare_key in item}
        
        # 过滤掉文件2中与文件1中相同的键值
        filtered_file2_data = [item for item in file2_data if compare_key in item and item[compare_key] not in file1_keys]
        
        # 将过滤后的数据写回文件2
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file2:
            json.dump(filtered_file2_data, file2, ensure_ascii=False, indent=4)
        print(f"Processed {file2_path} and saved to {output_path}")
    except FileNotFoundError:
        print(f"File {file1_path} or {file2_path} not found, skipping.")
    except KeyError:
        print(f"Key error in {file1_path} or {file2_path}, skipping.")
    except Exception as e:
        print(f"Error processing {file1_path} or {file2_path}: {e}")

# 遍历文件夹中的文件并处理
for server_type, file_configs in load_data.items():
    for file_name, keep_keys in file_configs.items():
        compare_key = keep_keys[0]  # 获取要对比的键
        file1_path = repo1_path / server_type / file_name
        file2_path = repo2_path / server_type / file_name
        output_path = repo2_path / server_type / file_name
        
        if file1_path.exists() and file2_path.exists():
            compare_and_process(file1_path, file2_path, output_path, compare_key)
        else:
            print(f"File {file1_path} or {file2_path} not found, skipping.")
