import pymongo
import jieba
from gensim.models import Word2Vec
from pprint import pprint

client = pymongo.MongoClient('localhost',27017)
db = client["JD"]
collection = db["item_info"]

item_id = 5706771

info = collection.find({'item_id': item_id})[0]["item_info"]

model = Word2Vec.load("wordvec.model")

def phrase_similarity(sentence, phrase):
    sim_list = []
    print(sentence, phrase)
    for word in phrase:
        max_sim = 0
        for word_s in sentence:
            try:
                model["word"]
                max_sim = max(max_sim, model.similarity(word,word_s))
            except:
                print(word,"not found.")
                continue

        sim_list.append(max_sim)
    sim_list.sort(reverse = True)
    ratio = 1
    ratio_sum = 0
    similarity = 0
    dec_rate = 5
    for sim in sim_list:
        ratio_sum = ratio_sum + ratio
        similarity = similarity + sim*ratio
        ratio = ratio/dec_rate
    return similarity/ratio_sum

def KB_answer(question):
    question = list(jieba.cut(question))
    calc_list = []
    for key_1 in info:
        group_label = list(jieba.cut(key_1))
        for key_2 in info[key_1]:
            label = list(jieba.cut(key_2))
            result = list(jieba.cut(info[key_1][key_2]))
            calc = phrase_similarity(question, label)
            #print(key_1,key_2,info[key_1][key_2],calc)
            calc_list.append((calc,key_1,key_2,info[key_1][key_2]))

    calc_list.sort(reverse = True,key=lambda x:x[0])
    pprint(calc_list[0:3])

KB_answer("前置摄像头像素是多少？")    
        
    
