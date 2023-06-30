import os, sys

def civitai_param_format(in_txt):
    lines_formatted = []

    # read from in_txt
    lines_split = []
    with open(in_txt, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if len(lines) <=3 and line.startswith('Steps: '):
                lines_split = line.split(',')
            else:
                lines_formatted.append(line)

    for line in lines_split:
        # skip empty line
        if line.strip() == '':
            continue

        line_formatted = line.strip() + ',\n'
        lines_formatted.append(line_formatted)

    # write to in_txt
    with open(in_txt, 'w') as file:
        file.writelines(lines_formatted)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: civitai-param-format.py <txt>")
        sys.exit(1)

    txt_path = sys.argv[1]
    print('txt: ' + txt_path)
    
    # for debug
    # txt_path = r'C:\11111.txt'
    
    civitai_param_format(txt_path)
