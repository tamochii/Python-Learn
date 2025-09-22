import os

# 获取当前目录下的所有 .ass 文件，并按名称降序排序
files = sorted([f for f in os.listdir() if f.endswith('.ass')], reverse=True)

# 确保文件数量符合预期
if len(files) != 24:
    print(f"警告：文件数量 {len(files)}，不等于 24，可能导致命名错误！")

# 目标文件名格式
new_format = "[VCB-Studio] Tokyo Ghoul Re [{:02d}][Ma10p_1080p][x265_flac].ass"

# 逐个重命名
for index, old_name in enumerate(files, start=1):
    new_name = new_format.format(index)
    os.rename(old_name, new_name)
    print(f'Renamed: {old_name} -> {new_name}')

print("重命名完成！")
