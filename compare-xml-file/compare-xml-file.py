import os, sys
import xml.dom.minidom as xml

def get_file_infos(in_xml):
    file_infos = {}

    # src: <file size=1573449 md5=fbaa544f8d66f835ba3ef6dff422eaf1>filename</file>
    # get file size, md5, filename
    with open(in_xml, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if not line.startswith('<file '):
                continue

            # get file size
            size = line.split('size=')[1].split(' ')[0]
            # get md5
            md5 = line.split('md5=')[1].split('>')[0]
            # get filename
            filename = line.split('>')[1].split('<')[0]

            file_infos[filename] = {'size': size, 'md5': md5}

    return file_infos

    
def print_dict_diff(in_dict1, in_dict2):
    for key, value in in_dict1.items():
        value2 = in_dict2.get(key)
        if value2 is None or value != value2:
            md5_1 = value.get('md5')
            md5_2 = 'None' if value2 is None else value2.get('md5')
            print('key: %s, md5_1: %s md5_2: %s' % (key, md5_1, md5_2 ))


def main():
    xml1 = sys.argv[1]
    xml2 = sys.argv[2]
    dict1 = get_file_infos(xml1)
    dict2 = get_file_infos(xml2)
    print_dict_diff(dict1, dict2)

if __name__ == '__main__':
    main()