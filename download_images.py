import requests

# 原始图片链接列表
image_urls = [
    "https://www.internationalsaimoe.com/img/posters/a/consolation-amethyst-2020.png",
    "https://www.internationalsaimoe.com/img/posters/a/consolation-amethyst-2021.png",
]

# 替换的关键字列表
replacements = ["aquamarine", "diamond", "emerald","ruby","sapphire","topaz","yamethyst","yaquamarine","ydiamond","yemerald","yruby","ysapphire","ytopaz"]

# 循环替换关键字
for replacement in replacements:
    # 新的图片链接列表
    new_image_urls = [url.replace("amethyst", replacement) for url in image_urls]
    
    # 下载图片
    for url in new_image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            # 提取文件名
            file_name = url.split("/")[-1]
            # 写入文件
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {url}")
