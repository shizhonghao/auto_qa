import jieba # word segmentation module

import warnings # simply ignore the problems caused by import gensim
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

#import gensim.models.word2vec as w2v
from gensim import corpora
from gensim.similarities import Similarity
from pprint import pprint

def find_simillar(sentence):
    pass

sentences = []
with open(r"C:\Users\施中昊\Desktop\实验室\auto_qa\segmentation.txt","r") as f:
    last_line = ''
    for line in f:
        sentences.append(line.split(' '))
        last_line = line.split(' ')
    print('input done')
    #pprint(sentences)
    # 生成字典和向量语料
dictionary = corpora.Dictionary(sentences)
corpus = [dictionary.doc2bow(text) for text in sentences]
index = Similarity('-Similarity-index', corpus, num_features=400)
print("training done:",last_line[:-1])
    
    # try to find the most similar centence
test_data = last_line[:-1]
test_corpus = dictionary.doc2bow(test_data)
index.num_best = 5
result = index[test_corpus]
print("find similarity")
print(result)
