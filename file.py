import os
import shutil

source_dir = r'F:\1_wrok\Topaz\TopazGigapixelAi\OutPut'

# 创建年份文件夹
for year in range(2008, 2023):
    os.makedirs(os.path.join(source_dir, str(year)), exist_ok=True)

# 遍历文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    print(f'检查文件: {filename}')  # 调试信息

    if os.path.isfile(file_path):
        moved = False  # 标记是否移动
        for year in range(2008, 2023):
            if str(year) in filename:
                shutil.move(file_path, os.path.join(source_dir, str(year), filename))
                print(f'移动文件: {filename} 到 {year} 文件夹')  # 调试信息
                moved = True
                break
        if not moved:
            print(f'没有匹配的年份: {filename}')  # 调试信息
print('文件分类完成！')
