import os
import sys
import time

def make_sub_file(in_lines, in_head, in_src_name, in_sub):
    [des_filename, extname] = os.path.splitext(in_src_name)
    filename  = des_filename + '_' + str(in_sub) + extname
    print( 'make file: %s' %filename)
    fout = open(filename,'w')
    try:
        fout.writelines([in_head])
        fout.writelines(in_lines)
        return in_sub + 1
    finally:
        fout.close()

def split_by_line_count(in_filename, in_count):
    fin = open(in_filename,'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == in_count:
                sub = make_sub_file(buf,head,in_filename,sub)
                buf = []
        if len(buf) != 0:
            sub = make_sub_file(buf,head,in_filename,sub)   
    finally:
        fin.close()

def main():
    begin = time.time()
    txt_path = sys.argv[1]
    print(txt_path)
    split_by_line_count(txt_path,600000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))

if __name__ == '__main__':
    main()
