import tarfile
import os
import glob

os.chdir("BAR")

def extract_files():
    Path = ''
    files = tarfile.open("Path_where_you_save_the_BAR_dataset")
    files.extractall()    
    return files 

if __name__ == "__main__":
    extract_files()

