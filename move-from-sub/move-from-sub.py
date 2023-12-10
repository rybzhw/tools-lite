# move sub directories to parent directory
import os, sys
import shutil

# loop through all sub directories
def move_from_sub(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if root != path:
                src = os.path.join(root, file)
                dst = os.path.join(path, file)
                # move file
                if not os.path.exists(dst):
                    shutil.move(src, dst)
                    print("Moved: {} -> {}".format(src, dst))
                else:
                    print("Exists: " + dst)

if __name__ == "__main__":
    # move_from_sub("TestInput")
    if len(sys.argv) < 2:
        print("Usage: move-from-sub.py <parent-path>")
        sys.exit(1)

    move_from_sub(sys.argv[1])
