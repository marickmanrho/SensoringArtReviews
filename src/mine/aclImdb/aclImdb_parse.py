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

    # Find filename and extract rating
    for file in os.listdir(path):
        if file.endswith(".txt"):
            if (file.find(str(id)+"_") != -1):
                partitioned = file.split("_")
                if partitioned[0] == str(id):
                    filename = file
                    rating = float(partitioned[1].split(".")[0])
                    break

    # Read filename
    with open(os.path.join(path,filename)) as file:
        text = file.read()

    # strip HTML tags
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text, features="html.parser")
    text = soup.get_text()

    return text, rating

class aclImdb_single():
    def __init__(self,path,id):
        [self.text, self.rating] = aclImdb_read_single(path,id)

    def sent(self):
        from nltk.tokenize import sent_tokenize
        return sent_tokenize(self.text)

    def words(self):
        from nltk.tokenize import word_tokenize
        return word_tokenize(self.text)

    def words_minimal(self):
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize

        wordlist = self.words()
        text_nopunct = [word.lower() for word in wordlist if word.isalpha()]
        text_nostop = [word for word in text_nopunct if word not in stopwords.words('english')]

        from nltk.stem import PorterStemmer
        stemming = PorterStemmer()
        text_stemmed = [stemming.stem(word) for word in text_nostop]
        return text_stemmed

if __name__ == '__main__':
    path = "D://databases/aclImdb/train/neg"
    id = 3
    single = aclImdb_single(path,id)
    print(single.__dict__)

    print(single.sent())

    print(single.words())

    print(single.words_nostop())
