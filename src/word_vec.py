import jieba # word segmentation module

import warnings # simply ignore the problems caused by import gensim
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim.models.word2vec as w2v

with open(r"C:\Users\施中昊\Desktop\实验室\auto_qa\segmentation.txt","r") as f:
    sentences = []
    for line in f:
        sentences = sentences + line.split(' ')
    model = w2v.Word2Vec(sentences, min_count=1) # here if min_count is too big, you`ll meet `RuntimeError: you must first build vocabulary before training the model` 
    model.save("train.model")
    
    print(model["有"])
