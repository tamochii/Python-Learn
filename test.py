import os
from PIL import Image

# 设置输入和输出文件夹路径
input_folder = r'C:\Users\tamochi\Desktop\in'
output_folder = r'C:\Users\tamochi\Desktop\out'

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 支持的图片格式
supported_formats = ('.jpg', '.jpeg', '.png')

# 遍历输入文件夹中的文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.webp'
        output_path = os.path.join(output_folder, output_filename)

        try:
            with Image.open(input_path) as img:
                # 将图片转换为 RGB 模式（如果不是）
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # 保存为 WebP 格式，设置质量为 80
                img.save(output_path, 'webp', quality=100)
                print(f'转换成功: {filename} -> {output_filename}')
        except Exception as e:
            print(f'转换失败: {filename}，错误信息: {e}')
