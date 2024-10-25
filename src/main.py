import os
import shutil


def copy_contents(src_dir, dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    else:
        os.mkdir("./public/")
    files = os.listdir("./static/")
    
    



def main():
    copy_contents("./static/", "./public/")



if __name__ == "__main__":
    main()