import os

# 指定输出日志的txt文件
log_file = 'files.txt'

# 指定要扫描的文件夹路径
path = 'C:\Users\Administrator\Desktop\Test\source\preparation'
dir_name = 'preparation'
dir_path = os.path.join(path, dir_name)

with open(log_file, 'w') as f:
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            f.write(filename + '\n')