import os
import shutil


def resort_dir(directory, sort_key=lambda x: x.lower()):
    """
    重新组织目录中的文件，按照给定的排序键进行排序。

    :param directory: 要重新组织的目录路径。
    :param sort_key: 一个函数，用于确定排序顺序。默认为按文件名小写字母排序。
    """
    # 获取目录中所有文件的名称
    files = os.listdir(directory)

    # 对文件名进行排序
    sorted_files = sorted(files, key=sort_key)

    # 创建一个临时目录来存放重新排序后的文件
    temp_dir = os.path.join(directory, '.temp_resort')
    os.makedirs(temp_dir, exist_ok=True)

    # 将文件移动到临时目录，同时保持排序顺序
    for filename in sorted_files:
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # 确保是文件而不是目录
            shutil.move(file_path, temp_dir)

            # 删除原始目录中的文件（除了子目录）
    for filename in files:
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

            # 将临时目录中的文件移回原始目录
    for filename in sorted_files:
        temp_file_path = os.path.join(temp_dir, filename)
        shutil.move(temp_file_path, directory)

        # 删除临时目录
    os.rmdir(temp_dir)


# 使用示例：
# 假设你有一个名为'my_dir'的目录，其中包含一些文件，你想要按文件名排序它们
directory_path = 'path/to/your_dir'
resort_dir(directory_path)