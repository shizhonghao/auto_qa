import jieba  # word segmentation module

import warnings  # simply ignore the problems caused by import gensim

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

# import gensim.models.word2vec as w2v
from gensim import corpora
from gensim.similarities import Similarity
from pprint import pprint


# 返回答案
def find_answer(question):
    # 对输入的问题进行分词
    question.replace('\t', '').replace(' ', '')  # .replace('\n', '')
    questionList = jieba.cut(question)
    print(question)
    # 建立问题和回答的字典
    dic = {}
    with open(r"C:\\Users\施中昊\Desktop\\2017 coding\jd_scrapy\sentence.txt") as question:
        with open(r"C:\\Users\施中昊\Desktop\\2017 coding\jd_scrapy\answer.txt") as answer:
            for q, a in zip(question, answer):
                dic[q] = a
    # 读取已经完成分词的语料库
    sentences = []
    with open(r"C:\Users\施中昊\Desktop\实验室\auto_qa\segmentation.txt", "r") as f:
        for line in f:
            sentences.append(line.split(' '))
        print('input done')
    # 生成字典和向量语料
    dictionary = corpora.Dictionary(sentences)
    corpus = [dictionary.doc2bow(text) for text in sentences]
    index = Similarity('-Similarity-index', corpus, num_features=400)
    print("training done:", questionList)
    # 找到与提出的问题最相似的已有问题
    resultList = find_simillar(questionList, dictionary, index)
    # 将得到的答案整合到一个List中并返回
    answerList = []
    for answer in resultList:
        # answerList.append(''.join(sentences[answer[0]]))
        answerList.append(dic[''.join(sentences[answer[0]])])
        #print(dic[''.join(sentences[answer[0]])])
    print(answerList)
    return answerList


# 寻找句子中前best_num的语料
def find_simillar(sentence, dictionary, index, best_num=5):
    corpus_find = dictionary.doc2bow(sentence)
    index.num_best = best_num
    result = index[corpus_find]
    return result


'''
sentences = []
with open(r"F:\programme\python\auto_qa\segmentation.txt","r") as f:
    last_line = ''
    for line in f:
        print(last_line)
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
#print(find_simillar(test_data))
result = find_simillar(test_data)
for linNum in result:
    print(''.join(sentences[linNum[0]]),linNum[1])
'''
if __name__ == '__main__':
    find_answer("什么叫双卡双待单通？可以同时插移动和联通的卡，用联通的卡上网吗？")
