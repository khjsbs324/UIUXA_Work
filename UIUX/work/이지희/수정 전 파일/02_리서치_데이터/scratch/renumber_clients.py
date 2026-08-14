import os
import re

client_dir = r'C:\UIUX이지희\Antigravity\클라이언트 분석'

files = [f for f in os.listdir(client_dir) if f.endswith('.md')]

# Sort files by their current numbers
def file_num(fname):
    m = re.search(r'\d+', fname)
    return int(m.group(0)) if m else 0

files.sort(key=file_num)

print(f"Found {len(files)} files to renumber:")

renamed_info = []

for idx, old_fname in enumerate(files, start=1):
    new_num_str = f"{idx:02d}"
    
    # Replace old [클라이언트XX] prefix with new [클라이언트YY]
    new_fname = re.sub(r'\[클라이언트\d+\]', f'[클라이언트{new_num_str}]', old_fname)
    
    old_path = os.path.join(client_dir, old_fname)
    new_path = os.path.join(client_dir, new_fname)
    
    # Read file content and update top header report number if present
    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update header e.g. # 가상클라이언트 기반 분석 결과 보고서 [03] -> # 가상클라이언트 기반 분석 결과 보고서 [02]
    new_content = re.sub(
        r'#\s*가상클라이언트\s*기반\s*분석\s*결과\s*보고서\s*\[\d+\]',
        f'# 가상클라이언트 기반 분석 결과 보고서 [{new_num_str}]',
        content
    )
    
    # Write updated content
    with open(old_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    # Rename file
    if old_path != new_path:
        os.rename(old_path, new_path)
        
    renamed_info.append((old_fname, new_fname, new_num_str))
    print(f"{idx:02d}. {old_fname} -> {new_fname}")

print("\nRenumbering and header update completed successfully!")
