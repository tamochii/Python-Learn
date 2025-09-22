import os

# 设置文件夹创建的父目录
parent_dir = r"D:\~tamochi~\败北女角太多了\插图"  # 使用原始字符串

# 创建文件夹
for year in range(1, 6):
    folder_name = f"败北女角太多了!{year}"
    folder_path = os.path.join(parent_dir, folder_name)
    
    try:
        os.makedirs(folder_path)
        print(f"创建文件夹: {folder_path}")
    except FileExistsError:
        print(f"文件夹已存在: {folder_path}")
    except Exception as e:
        print(f"创建文件夹时出错: {e}")
