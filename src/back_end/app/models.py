import pymongo
import jieba
from gensim.models import Word2Vec
from pprint import pprint

item_id = 5706771

#info = collection.find({'item_id': item_id})[0]["item_info"]

#model = Word2Vec.load("app/text_processor/wordvec.model")

#get the information of a particular item whose id is id
def getItemInfo(id):
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    set = db["item_info"]
    info = set.find({'item_id':id})[0]
    client.close()
    return info

#get those questions and corresponding answers of a particular item whose id is id
def getSellerQA(id):
    client = pymongo.MongoClient('localhost', 27017)
    db = client["JD"]
    set = db["seller_qa"]
    ret = set.find({'item_id':id})[0]['seller_qa']
    client.close()
    return ret

#add a new pair of question and answer to a particular item
def updateQA(id,question,answer):
    qaDict = {}
    qaDict['question'] = question
    qaDict['answer'] = answer
    client = pymongo.MongoClient('localhost', 27017)
    db = client["JD"]
    set = db["seller_qa"]
    oldDict = []
    oldDict = set.find({'item_id':id})[0]['seller_qa']
    #print(type(oldDict))
    oldDict.append(qaDict)
    #print(oldDict)
    set.update({'item_id':id},{'$set':{'seller_qa':oldDict}})
    client.close()

#add unanswered question into database
def newQuestion(question):
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    set = db["new_question"]
    set.insert({"question":question})
    client.close()

#get unanswered question from the database
def getNewQ():
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    set = db["new_question"]
    result = set.find()
    questionList = []
    for dict in result:
        questionList.append(dict['question'])
    client.close()
    return questionList

#delete the question who has been newly answered
def delQ(question):
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    set = db["new_question"]
    set.delete_one({"question":question})

if __name__ == '__main__':
    #newQuestion("test")
    delQ('test')
    info = getNewQ()
    print(info)