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

# 提取文件并清理
def extract_and_clean_files(repo_path, temp_path, zip_files):
    for zip_file in zip_files:
        zip_file_path = repo_path / zip_file
        if zip_file_path.exists():
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # 根据zip文件名确定服务器类型
                server_type = Path(zip_file).stem.split("原版DB")[0]
                zip_temp_path = temp_path / server_type
                zip_temp_path.mkdir(parents=True, exist_ok=True)
                for file in zip_ref.namelist():
                    if file.endswith(".json"):
                        zip_ref.extract(file, zip_temp_path)
                        # 清理JSON文件
                        clean_json_file(zip_temp_path / file, load_data[server_type].get(file, []))
        else:
            print(f"Zip file {zip_file} not found in {repo_path}, skipping.")

# 清理JSON文件
def clean_json_file(file_path, keep_keys):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        cleaned_data = clean_json(json_data, keep_keys)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
        print(f"Cleaned {file_path}")
    except FileNotFoundError:
        print(f"File {file_path} not found, skipping.")
    except json.JSONDecodeError:
        print(f"File {file_path} is not a valid JSON file, skipping.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# 清理JSON数据
def clean_json(data, keep_keys):
    if isinstance(data, dict):
        cleaned_data = {}
        for key, value in data.items():
            if key in keep_keys:
                cleaned_data[key] = clean_json(value, keep_keys)
        return cleaned_data
    elif isinstance(data, list):
        return [clean_json(item, keep_keys) for item in data]
    else:
        return data

# 获取仓库1中的zip文件列表
repo1_zip_files = [file.name for file in repo1_path.glob("*.zip")]

# 提取仓库1的文件
extract_and_clean_files(repo1_path, temp_path, repo1_zip_files)

# 获取仓库2中的zip文件列表
repo2_zip_files = [file.name for file in repo2_path.glob("*.zip")]

# 提取仓库2的文件
extract_and_clean_files(repo2_path, temp_path, repo2_zip_files)

# 比较文件并处理
def compare_and_process(file1_path, file2_path, output_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1:
            file1_data = json.load(file1)
        with open(file2_path, 'r', encoding='utf-8') as file2:
            file2_data = json.load(file2)
        
        # 获取文件1中所有的键
        file1_keys = set()
        for item in file1_data:
            item_tuple = tuple((k, v) for k, v in item.items() if not isinstance(v, list))
            file1_keys.add(item_tuple)
        
        # 过滤掉文件2中与文件1中相同的键
        filtered_file2_data = []
        for item in file2_data:
            item_tuple = tuple((k, v) for k, v in item.items() if not isinstance(v, list))
            if item_tuple not in file1_keys:
                filtered_file2_data.append(item)
        
        # 将过滤后的数据写回文件2
        with open(output_path, 'w', encoding='utf-8') as file2:
            json.dump(filtered_file2_data, file2, ensure_ascii=False, indent=4)
        print(f"Processed {file2_path} and saved to {output_path}")
    except FileNotFoundError:
        print(f"File {file1_path} or {file2_path} not found, skipping.")
    except KeyError:
        print(f"Key error in {file1_path} or {file2_path}, skipping.")

# 遍历临时文件夹中的文件并处理
for server_type in load_data.keys():
    repo_temp_path = temp_path / server_type
    for zip_folder in repo_temp_path.iterdir():
        if zip_folder.is_dir():
            for file in zip_folder.iterdir():
                if file.name.endswith(".json"):
                    file1_path = temp_path / server_type / zip_folder.name / file.name
                    file2_path = temp_path / server_type / zip_folder.name / file.name
                    output_path = repo2_path / server_type / zip_folder.name / file.name
                    if file1_path.exists() and file2_path.exists():
                        compare_and_process(file1_path, file2_path, output_path)
                    else:
                        print(f"File {file1_path} or {file2_path} not found, skipping.")
