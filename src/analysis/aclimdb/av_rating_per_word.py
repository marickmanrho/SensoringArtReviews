def av_rating_per_word():
    import numpy as np

    import pandas as pd
    word_rating = pd.DataFrame(data={'word':[],'rating_sum':[],'count':[]})

    print(word_rating)

    from src.mine.aclImdb.aclImdb_parse import aclImdb_single
    path = "D://databases/aclImdb/train/neg"

    # Read negative reviews
    Nnegrev = 100
    for id in range(Nnegrev):
        # read review
        rev = aclImdb_single(path,id)

        # tokenize
        words = rev.words_minimal()

        # save words with rating and count
        data = pd.DataFrame({   'word':words,\
                                'rating_sum':np.ones(len(words))*rev.rating, \
                                'count':np.ones(len(words))})

        # append words
        word_rating = word_rating.append(data,ignore_index=True)

    # sum words when equal
    word_rating = word_rating.groupby(['word']).agg({'rating_sum':'sum','count':'sum'})

    print(word_rating.sort_values(by=['count'],ascending=False))
    print(word_rating.sort_values(by=['rating_sum'],ascending=False))
    # Read positive reviews

    pass

# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    print(dir(path[0]))
    path.append("D://Repositories/SensoringArtReviews")

if __name__ == '__main__':
    av_rating_per_word()
