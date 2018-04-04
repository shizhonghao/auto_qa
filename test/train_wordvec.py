import jieba
from gensim.models import Word2Vec
from pprint import pprint


"""
class get_sentences(object):
    def __init__(self, dir_list):
        self.dir_list = dir_list

    def __iter__(self):
        for file_name in self.dir_list:
            with open(file_name,"r",encoding = 'utf-8') as file:
                for line in file:
                    seg_list = list(jieba.cut(line))
                    yield seg_list

dir_list = [
            r'C:/Users/施中昊/Desktop/2017 coding/jd_scrapy/sentence.txt',
            r'C:/Users/施中昊/Desktop/2017 coding/jd_scrapy/answer.txt',
            r'C:/Users/施中昊/Desktop/2017 coding/jd_scrapy/buyerQ.txt'
            ]
sentence = get_sentences(dir_list)
model = Word2Vec(sentence, min_count = 1,size = 200)



"""
sentence = []
with open(r'C:/Users/施中昊/Desktop/2017 coding/jd_scrapy/sentence.txt','r',encoding = 'utf-8') as f:
    for line in f:
        seg_list = jieba.cut(line)
        sentence.append([x for x in seg_list])

with open(r'C:/Users/施中昊/Desktop/2017 coding/jd_scrapy/answer.txt','r',encoding = 'utf-8') as f:
    for line in f:
        seg_list = jieba.cut(line)
        sentence.append([x for x in seg_list])

with open(r'C:/Users/施中昊/Desktop/2017 coding/jd_scrapy/buyerQ.txt','r',encoding = 'utf-8') as f:
    for line in f:
        seg_list = jieba.cut(line)
        sentence.append([x for x in seg_list])

    #pprint(sentence)
    model = Word2Vec(sentence, min_count = 1, size=200)
    model.save("wordvec.model")

#"""
