import shutil
from pathlib import Path
import datetime
import os

ROOT = r'\\Omv01\成人内容\未整理'

START_PATH = r'\\Omv01\成人内容\未整理'

MOVE_FILE_TYPE = {'.MP4', '.AVI', '.pdf', '.mkv', '.bmp', '.wma', '.gif', '.jpg', '.PNG', '.m1v', '.mp3', '.JPG',
                  '.WAV', '.avi', '.wmv', '.WMA', '.png', '.MOV', '.rm',
                  '.flv', '.zip', '.asf', '.rar', '.MPG', '.wav', '.mp4'}


def move_file(file, directory):
    if not Path(Path(directory).joinpath(file.name)).exists():
        shutil.move(str(file), directory)
    else:
        shutil.move(str(file), Path(directory).joinpath(str(datetime.datetime.now().timestamp()) + Path(file).name))


def flat_file(path):
    # 列出目录下的所有文件
    current_path = Path(path).iterdir()
    for file_or_directory in current_path:
        # 对数组里面每个元素进行判断,如果是目录,则递归
        if Path.is_dir(file_or_directory):
            flat_file(file_or_directory)
            # 待内部文件全部完成后,删除该目录
            shutil.rmtree(file_or_directory)
        # 如果是文件,则判断在根目录下是否已有同名文件,如果已有,则加个时间戳,否则直接移动
        else:
            # 如果扩展名在设置的移动范围内,则进行移动操作
            if Path(file_or_directory).suffix in MOVE_FILE_TYPE:
                move_file(file_or_directory, ROOT)
            else:
                continue


file_type_set = set()


# 列出某目录下所有的文件扩展名
def show_all_file_type(path):
    # 列出目录下的所有文件
    current_path = Path(path).iterdir()
    # 遍历每个对象,判断对象的类型
    for file_or_directory in current_path:
        # 如果是目录,则递归
        if Path.is_dir(file_or_directory):
            show_all_file_type(file_or_directory)
        # 如果是文件,则将文件类型加入set
        else:
            file_type_set.add(Path(file_or_directory).suffix)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flat_file(START_PATH)
