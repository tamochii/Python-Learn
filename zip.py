import os
import zipfile

def safe_unzip(zip_path, extract_to):
    # 1. 检查文件是否存在
    if not os.path.isfile(zip_path):
        print(f'❌ 错误：文件不存在 -> {zip_path}')
        return
    
    # 2. 检查是否为有效的 zip
    if not zipfile.is_zipfile(zip_path):
        print(f'❌ 错误：这不是一个合法的 ZIP 文件，请确认格式或文件是否损坏。')
        return

    # 3. 确保目标文件夹存在
    os.makedirs(extract_to, exist_ok=True)
    
    # 4. 执行解压
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(extract_to)
        print(f'✅ 成功解压：{zip_path} -> {extract_to}')
    except Exception as e:
        print(f'❌ 解压失败，错误信息：{e}')

if __name__ == '__main__':
    zip_path    = r'C:\Users\tamochi\Downloads\test.zip'
    extract_to = r'C:\Users\tamochi\Downloads\test_folder'
    safe_unzip(zip_path, extract_to)
