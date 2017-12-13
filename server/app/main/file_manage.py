import os
basedir = os.path.abspath(os.path.dirname(__file__))

class FileManage:

    def __init__(self):
        pass

    def search_dir(self):
        dir = basedir + '\\..\\static\\image'
        print(dir)
        files = os.listdir(dir)
        return files

