def aclImdb_read():
    version = '0.0'

    import argparse
    parser = argparse.ArgumentParser(prog='yale_imdb_read', usage='python3 yi_read.py [options]')
    parser.add_argument('-I', default='default', help='Path to database folder aclImdb/.')
    parser.add_argument('-v', action='store_true', help='Run verbose mode.')
    parser.add_argument('--version', action='version', version='%(prog)s v.'+version)
    args = parser.parse_args()

    import pandas as pd

    pass

def aclImdb_read_single(path,id):
    import os

    for file in os.listdir(path):
        if file.endswith(".txt"):
            if (file.find(str(id)+"_") != -1):
                partitioned = file.split("_")
                if partitioned[0] == str(id):
                    filename = file
                    rating = partitioned[1].split(".")[0]
                    break

    with open(os.path.join(path,filename)) as file:
        text = file.read()

    return text, rating

class aclImdb_single():
    def __init__(self,path,id):
        [self.text, self.rating] = aclImdb_read_single(path,id)

if __name__ == '__main__':
    path = "D://databases/aclImdb/train/neg"
    id = 3
    single = aclImdb_single(path,id)
    print(single.__dict__)
