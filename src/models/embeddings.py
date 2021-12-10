# Word embedding
import gensim
# word2vec_path = '../../models/bio_embedding_extrinsic'
# w2v_model = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)

import numpy as np

class MeanEmbeddingVectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = word2vec.vector_size

    def fit(self, X, y):
        return self

    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0) # for oov
            for words in X
        ])
