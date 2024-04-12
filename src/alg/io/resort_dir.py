import os
import shutil

def copy_files(source_folder, destination_folder):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 遍历源文件夹中的文件
    for root, _, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(root, filename)
            destination_path = os.path.join(destination_folder, filename)
            if os.path.exists(destination_path):
                # 如果目标文件已存在，则添加索引以避免重名
                idx = 1
                while True:
                    new_filename = f"{os.path.splitext(filename)[0]}_{idx}{os.path.splitext(filename)[1]}"
                    new_destination_path = os.path.join(destination_folder, new_filename)
                    if not os.path.exists(new_destination_path):
                        destination_path = new_destination_path
                        break
                    idx += 1
            # 复制文件到目标文件夹
            shutil.copy2(source_path, destination_path)


source_folder = "你的源文件夹路径"
destination_folder = "你要复制到的目标文件夹路径"

copy_files(source_folder, destination_folder)
