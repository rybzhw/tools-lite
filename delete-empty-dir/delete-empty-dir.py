# delete empyt directories
import os, sys

# delete empty directories recursively
def delete_empty_dir_recursively(path):
    # loop through all sub directories
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            if os.path.isdir(dir_path) and not os.listdir(dir_path):
                os.rmdir(dir_path)
                print("Deleted: " + dir_path)
                
# delete empty directories only first level
def delete_empty_dir(path):
    for dir in os.listdir(path):
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path) and not os.listdir(dir_path):
            os.rmdir(dir_path)
            print("Deleted: " + dir_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: delete-empty-dir.py <path>")
        sys.exit(1)

    delete_empty_dir(sys.argv[1])
