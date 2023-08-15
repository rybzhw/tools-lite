import os,sys
import time
import subprocess

cur_path = os.path.dirname(os.path.abspath(__file__))
print(cur_path)

def read_config():
    ext_to_property_dict = {}

    config_path = os.path.join(cur_path, 'config.ini')
    with open(config_path, 'r') as file:
        for line in file.readlines():
            ext = line.split('=')[0].split('*')[1].strip()
            property = line.split('=')[1].split('\n')[0]
            ext_to_property_dict[ext] = property

    return ext_to_property_dict

def scan_files(in_svn_path):
    ext_to_property_dict = read_config()

    os.chdir(in_svn_path)
    # 遍历 svn 仓库目录下的所有文件和文件夹
    for dirpath, dirnames, filenames in os.walk(in_svn_path):
        # skip .svn dir
        if '.svn' in dirpath:
            continue

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # get file extent
            file_ext = os.path.splitext(filename)[1]
            if file_ext in ext_to_property_dict:
                check_needs_lock(file_path)
                continue

def check_needs_lock(file_path):
    # 执行 svn propget 命令，检查文件是否包含 svn:needs-lock 属性
    cmd = ['svn', 'propget', 'svn:needs-lock', file_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    # 如果没有包含 svn:needs-lock 属性，则执行 svn propset 命令来增加该属性
    if result.returncode != 0:
        print('add svn:needs-lock property to {}'.format(file_path))
        cmd = ['svn', 'propset', 'svn:needs-lock', 'true', file_path]
        subprocess.run(cmd)

def main():
    svn_path = sys.argv[1]
    print(svn_path)

    # just for debug
    # svn_path = r'I:\p4tosvn\trunk_2023'

    begin = time.time()
    scan_files(svn_path)
    end = time.time()
    print('time is %d seconds ' % (end - begin))

if __name__ == '__main__':
    main()
