import json
import os
import zipfile
from pathlib import Path

# 定义需要提取的文件
files_to_extract = [
    "CharacterDialogEmojiExcel.json",
    "CharacterDialogEventExcel.json",
    "CharacterDialogExcel.json",
    "LocalizeErrorExcel.json",
    "LocalizeEtcExcel.json",
    "LocalizeExcel.json",
    "LocalizeSkillExcel.json",
    "ScenarioCharacterNameExcel.json",
    "ScenarioScriptExcel.json",
    "TutorialCharacterDialogExcel.json"
]

# 定义仓库路径
repo1_path = Path(".")
repo2_path = Path("BA-Text")

# 创建临时文件夹
temp_path = Path("temp")
temp_path.mkdir(exist_ok=True)

def extract_all_files(zip_path, extract_to):
    """Extract all target files from a zip, preserving their internal structure"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in files_to_extract:
            # Find the file in the zip regardless of its internal path
            for zip_info in zip_ref.infolist():
                if zip_info.filename.endswith(file):
                    # Preserve the internal directory structure
                    output_path = extract_to / Path(zip_info.filename)
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    zip_ref.extract(zip_info, extract_to)
                    # Rename to standardize path if needed
                    if output_path != extract_to / file:
                        (extract_to / zip_info.filename).rename(extract_to / file)
                    break

def process_repo(repo_path, temp_path, repo_name):
    """Process all zip files in a repository"""
    for zip_file in repo_path.glob("*.zip"):
        # Create a temp dir for this zip file
        zip_temp_path = temp_path / repo_name / zip_file.stem
        zip_temp_path.mkdir(parents=True, exist_ok=True)
        
        print(f"Extracting files from {zip_file}...")
        try:
            extract_all_files(zip_file, zip_temp_path)
        except Exception as e:
            print(f"Error processing {zip_file}: {str(e)}")

def compare_json(file1, file2, output_path):
    """Compare two JSON files and save unique entries from file2"""
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    
    # Create set of unique identifiers from file1
    file1_keys = set()
    for item in data1:
        # Create a hashable key from non-list values
        key = tuple((k, str(v)) for k, v in item.items() if not isinstance(v, list))
        file1_keys.add(key)
    
    # Filter file2 data
    filtered_data = [
        item for item in data2 
        if tuple((k, str(v)) for k, v in item.items() if not isinstance(v, list)) not in file1_keys
    ]
    
    # Save results
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)
    print(f"Saved filtered data to {output_path} ({len(filtered_data)}/{len(data2)} entries kept)")

def main():
    # Process both repositories
    print("Processing repository 1...")
    process_repo(repo1_path, temp_path, "repo1")
    
    print("\nProcessing repository 2...")
    process_repo(repo2_path, temp_path, "repo2")
    
    # Compare files
    print("\nComparing files...")
    for file in files_to_extract:
        # Find all extracted files in both repos
        repo1_files = list((temp_path / "repo1").rglob(file))
        repo2_files = list((temp_path / "repo2").rglob(file))
        
        if not repo1_files or not repo2_files:
            print(f"\nSkipping {file} - not found in both repositories")
            continue
            
        # Use the first matching file from each repo
        file1 = repo1_files[0]
        file2 = repo2_files[0]
        
        print(f"\nComparing {file}:")
        print(f"  Repo1: {file1}")
        print(f"  Repo2: {file2}")
        
        # Prepare output path in repo2
        output_path = repo2_path / file2.relative_to(temp_path / "repo2")
        
        try:
            compare_json(file1, file2, output_path)
        except Exception as e:
            print(f"Error comparing {file}: {str(e)}")

if __name__ == "__main__":
    main()
