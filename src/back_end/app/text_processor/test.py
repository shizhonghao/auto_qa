import jieba  # word segmentation module
#from app.text_processor.config import *
from config import *
#from app.models import *
import win_unicode_console
win_unicode_console.enable()

import warnings  # simply ignore the problems caused by import gensim
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

# import gensim.models.word2vec as w2v
from gensim import corpora
from gensim.similarities import Similarity
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import label_binarize
from numpy import argmax

#"C:/Users/施中昊/Desktop/实验室/auto_qa/test/similarity_out.txt"

# 判断问题是否可以用知识库数据解决,
# 输入用空格分隔的分词后的问题字符串
# 返回为int[0,1]：0（非KB_QA），1（可以用结构化信息回答）
def is_KB_QA(question):
    with open(CLARIFICATION_TRAIN, "r") as f:
        clf = svm.SVC(kernel='linear')
        sentence = []
        lable = []
        for line in f:
            # line = line.split()
            lable.append(int(line[0]))
            questionList = jieba.cut(line[2:-1])
            question_seg = " ".join(questionList)
            sentence.append(question_seg)

        #pprint(sentence)
        # 提取训练集特征
        count_vec = CountVectorizer()
        count_train = count_vec.fit_transform(sentence)

        # 保证测试数据与训练集的词典相同
        count_vec_2 = CountVectorizer(vocabulary=count_vec.vocabulary_)
        count_test = count_vec_2.fit_transform([question])
        print(count_train.shape, count_test.shape)

        # 由词频统计转为tf-idf模型
        tfidf_trans = TfidfTransformer()
        tfidf_train = tfidf_trans.fit(count_train).transform(count_train)
        tfidf_test = tfidf_trans.fit(count_test).transform(count_test)

        # 训练SVM模型
        clf.fit(tfidf_train, lable)

        result = clf.predict(tfidf_test)
        print(result)
        return result[0]

# 利用svm实现的多分类函数
def classify(question):
    model = OneVsRestClassifier(svm.SVC(kernel='linear'))
    with open(CLARIFICATION_TRAIN, "r") as f:
        sentence = []
        lable = []
        for line in f:
            # line = line.split()
            lable.append(int(line[0]))
            questionList = jieba.cut(line[2:-1])
            question_seg = " ".join(questionList)
            sentence.append(question_seg)
    wordCount = CountVectorizer()
    wordCntList = wordCount.fit_transform(sentence)
    label = label_binarize(lable,classes=list(range(3)))
    tfidfTrans = TfidfTransformer()
    tfidf_x = tfidfTrans.fit(wordCntList).transform(wordCntList)
    clf = model.fit(tfidf_x,label)
    qWordCount = CountVectorizer(vocabulary=wordCount.vocabulary_)
    qList = jieba.cut(question)
    qSeg = " ".join(qList)
    qCntList = qWordCount.fit_transform([qSeg])
    tfidf_q = tfidfTrans.fit(qCntList).transform(qCntList)
    types = argmax(clf.decision_function(tfidf_q),axis=1)[0]
    return types

# 比较一个短语与句子的匹配程度
# 短语比重从高到底排序后用反比例函数在i处的值确定
# 返回一个double[0,1]之间的匹配程度值
def phrase_similarity(sentence, phrase):
    sim_list = []
    for word in phrase:
        max_sim = 0
        for word_s in sentence:
            try:
                model[word]
                max_sim = max(max_sim, model.similarity(word, word_s))
            except:
                print(word, "not found.")
                continue

        sim_list.append(max_sim)
    sim_list.sort(reverse=True)
    ratio = 1
    ratio_sum = 0
    similarity = 0
    dec_rate = 5
    for sim in sim_list:
        ratio_sum = ratio_sum + ratio
        similarity = similarity + sim * ratio
        ratio = ratio / dec_rate
    return similarity / ratio_sum

# 返回最匹配得分最高的3个相似度大于90%的结构化信息,若不足则只返回部分结果
# 每条为一个4元组（匹配得分，参数分类，参数名称，参数内容）
def KB_answer(question):
    calc_list = []
    info = getItemInfo(item_id)
    for key_1 in info:
        group_label = list(jieba.cut(key_1))
        for key_2 in info[key_1]:
            label = list(jieba.cut(key_2))
            result = list(jieba.cut(info[key_1][key_2]))
            calc = phrase_similarity(question, label)
            # print(key_1,key_2,info[key_1][key_2],calc)
            calc_list.append((calc, key_1, key_2, info[key_1][key_2]))

    calc_list.sort(reverse=True, key=lambda x: x[0])
    pprint(calc_list[0:3])
    for i, answer in enumerate(calc_list[0:3]):
        if answer[0]<0.9:
            return calc_list[0:i]
    return calc_list[0:3]

# 返回一个问题的答案
def find_answer(question):
    # 对输入的问题进行分词
    question.replace('\t', '').replace(' ', '')  # .replace('\n', '')
    question_gen = jieba.cut(question)
    questionList = list(question_gen)
    question_seg = " ".join(questionList)
    print(question_seg)
    print(question,question_gen,questionList,question_seg)
    answerList = []

    # 判断问题是否可以用知识库数据解决
    if is_KB_QA(question_seg):
        print("Is KB QA:")
        info_list = KB_answer(questionList)
        for answer in info_list:
            answerDic = {}
            answerDic["answer"] = answer[2] + "为" + answer[3]
            answerDic["percentage"] = (int)(answer[0] * 100)
            answerList.append(answerDic)
    # 如果答案列表为空，在以回答的问题中寻找相似答案
    if not answerList:
        print("Is not KB QA:")
        # 建立问题和回答的字典
        dic = {}
        question,answer = getSellerQA(item_id)
        #with open(SENTENCE_PATH, "r", encoding="utf-8") as question:
        #    with open(ANSWER_PATH, "r", encoding="utf-8") as answer:
        for q, a in zip(question, answer):
            dic[q] = a
        # 读取已经完成分词的语料库
        sentences = []
        for line in question:
            line.replace('\t', '').replace(' ', '')  # .replace('\n', '')
            seg_list = jieba.cut(line)
            sentences.append(list(seg_list))
        print('input done')
        # 生成字典和向量语料
        #pprint(sentences)
        dictionary = corpora.Dictionary(sentences)
        corpus = [dictionary.doc2bow(text) for text in sentences]
        index = Similarity('-Similarity-index', corpus, num_features=400)
        print("training done:", list(question_gen))
        # 找到与提出的问题最相似的已有问题
        resultList = find_simillar(questionList, dictionary, index)
        # 将得到的答案整合到一个List中并返回
        for answer in resultList:
            answerDic = {}
            # answerList.append(''.join(sentences[answer[0]]))
            answerDic["answer"] = dic[''.join(sentences[answer[0]])]
            answerDic["percentage"] = (int)(answer[1]*100)
            answerList.append(answerDic)
            #answerList.append(dic[''.join(sentences[answer[0]])])
            #print(dic[''.join(sentences[answer[0]])])
        print(resultList)
    reDic = {}
    reDic["answer"] = answerList
    reDic["cnt"] = len(answerList)
    print(reDic)
    return reDic


# 寻找句子中前best_num的语料
def find_simillar(sentence, dictionary, index, best_num=5):
    corpus_find = dictionary.doc2bow(sentence)
    index.num_best = best_num
    result = index[corpus_find]
    return result

# 获取未作答的问题数列表
def get_questions():
    question_list = getNewQ()
    #question_list = [{"question":"问题1"},{"question":"问题2"}]
    print("in get_question")
    return {"question_list":question_list, "question_cnt":len(question_list)}

# 将作出的回答写入数据库中
def add_QA_pairs(question, answer):
    print(question, answer)
    updateQA(item_id,question,answer)
    delQ(question)
    pass

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
    #find_answer("什么叫双卡双待单通？可以同时插移动和联通的卡，用联通的卡上网吗？")
    #is_KB_QA("什么叫双卡双待单通？可以同时插移动和联通的卡，用联通的卡上网吗？")
    print(classify("什么叫双卡双待单通？可以同时插移动和联通的卡，用联通的卡上网吗？"))
