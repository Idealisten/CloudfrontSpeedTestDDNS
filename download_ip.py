import os

'''
# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# GitHub 项目的 URL
github_url = "https://github.com/hello-earth/cloudflare-better-ip"

# 指定本地文件夹的路径
local_folder_path = os.path.join(script_directory, "cloudflare-better-ip")

# 克隆 GitHub 项目到本地文件夹
repo = git.Repo.clone_from(github_url, local_folder_path)

print(f"GitHub 项目已成功克隆到本地文件夹: {local_folder_path}")
'''
# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 指定 cloudflare-better-ip 目录和 cloudfront 目录的路径
cloudflare_better_ip_folder = os.path.join(script_directory, "cloudflare-better-ip")
cloudfront_folder = os.path.join(cloudflare_better_ip_folder, "cloudfront")

# 指定合并后的文件路径
output_file_path = os.path.join(script_directory, "better_ip.txt")

# 遍历 cloudfront 目录下的所有 .txt 文件并合并到 ip.txt
with open(output_file_path, "w") as output_file:
    for root, _, files in os.walk(cloudfront_folder):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as txt_file:
                    lines = txt_file.readlines()
                    for line in lines:
                        # 使用冒号分割每行，然后取第一个部分并去除首尾空格
                        parts = line.split(":")
                        if len(parts) > 0:
                            data_to_keep = parts[0].strip()
                            # 写入处理后的数据到输出文件
                            output_file.write(data_to_keep + "\n")

print("所有 .txt 文件已合并并处理到 ip.txt 文件中。")


# 打开 cft.txt 文件以供读取
with open('cft.txt', 'r') as cf_file:
    cf_content = cf_file.read()

# 打开 ip.txt 文件以供追加
with open('better_ip.txt', 'r') as ip_file:
    # 将 cft.txt 的内容追加到 ip.txt 的末尾
    better_ip = ip_file.read()

with open('ip.txt', 'w') as all_ip_file:
    all_ip_file.write(cf_content)
    all_ip_file.write('\n')
    all_ip_file.write(better_ip)

print("cft.txt内容已成功追加到 ip.txt 文件中")



