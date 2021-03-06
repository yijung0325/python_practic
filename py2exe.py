import argparse
import os
import subprocess
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_py", type=str, help=".py file")
    args = parser.parse_args()
    file_py = args.file_py
    if not os.path.isfile(file_py):
        print("{} does not exist".format(file_py))
        return
    subprocess.check_output("pyinstaller -F {}".format(file_py), stderr=subprocess.STDOUT, shell=True)
    # move exe to local dir
    file_name = file_py[file_py.rfind('/')+1:-3]
    if os.path.isfile("dist/{}.exe".format(file_name)):
        shutil.move("dist/{}.exe".format(file_name), "./{}.exe".format(file_name))
    # remove ...
    os.remove("{}.spec".format(file_name))
    shutil.rmtree("build")
    shutil.rmtree("dist")
    return

if __name__ == "__main__":
    main()
