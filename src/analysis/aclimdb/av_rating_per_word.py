def av_rating_per_word():
    import numpy as np
    import pandas as pd

    path = "D://databases/aclImdb/train/neg"

    # Read negative reviews
    Nnegrev = 100

    word_rating = read_range(path,0,Nnegrev)
    #print(word_rating.sort_values(by='rating_sum', ascending=False))

    from data.sensory_words.sensory_words import sensory_words_class
    sw = sensory_words_class()

    print(word_rating.isin(sw.touch).sort_values(by='word'))
    exit()
    print(sw.sight)

def read_range(path,min,max):
    import pandas as pd
    import numpy as np
    from src.mine.aclImdb.aclImdb_parse import aclImdb_single

    wr = pd.DataFrame(data={'word':[],'rating_sum':[],'count':[]})
    word_rating = pd.DataFrame(data={'word':[],'rating_sum':[],'count':[]})

    for id in range(min,max):

        # read review
        rev = aclImdb_single(path,id)

        # tokenize
        words = rev.words_minimal()

        # save words with rating and count
        data = pd.DataFrame({   'word':words,\
                                'rating_sum':np.ones(len(words))*rev.rating, \
                                'count':np.ones(len(words))})

        # append words
        wr = wr.append(data,ignore_index=True)

        if (np.mod(id,10)==0 or id==max-1):
            q = wr.groupby(['word']).agg({'rating_sum':'sum','count':'sum'}).reset_index()
            word_rating = pd.concat([word_rating,q])
            wr = pd.DataFrame(data={'word':[],'rating_sum':[],'count':[]})

    # sum words when equal
    word_rating = word_rating.groupby(['word']).agg({'rating_sum':'sum','count':'sum'}).reset_index()

    return word_rating

# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    print(dir(path[0]))
    path.append("D://Repositories/SensoringArtReviews")

if __name__ == '__main__':
    av_rating_per_word()
