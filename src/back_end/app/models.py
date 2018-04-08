import pymongo
import jieba
from gensim.models import Word2Vec
from pprint import pprint

#5706771 4586850
item_id = 4835534

#info = collection.find({'item_id': item_id})[0]["item_info"]

model = Word2Vec.load("app/text_processor/wordvec.model")

#get the information of a particular item whose id is id
def getItemInfo(id):
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    sheet = db["item_info"]
    info = sheet.find({'item_id':id})[0]["item_info"]
    client.close()
    return info

#get those questions and corresponding answers of a particular item whose id is id
def getSellerQA(id):
    client = pymongo.MongoClient('localhost', 27017)
    db = client["JD"]
    sheet = db["seller_qa"]
    ret = sheet.find({'item_id':id})[0]['seller_qa']
    qList = []
    aList = []
    for dict in ret:
        qList.append(dict['question'])
        aList.append(dict['answer'])
    client.close()
    return qList,aList

#add a new pair of question and answer to a particular item
def updateQA(id,question,answer):
    qaDict = {}
    qaDict['question'] = question
    qaDict['answer'] = answer
    client = pymongo.MongoClient('localhost', 27017)
    db = client["JD"]
    sheet = db["seller_qa"]
    oldDict = []
    oldDict = sheet.find({'item_id':id})[0]['seller_qa']
    #print(type(oldDict))
    oldDict.append(qaDict)
    #print(oldDict)
    sheet.update({'item_id':id},{'$set':{'seller_qa':oldDict}})
    client.close()

#add unanswered question into database
def newQuestion(question):
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    sheet = db["new_question"]
    sheet.insert({"question":question})
    client.close()

#get unanswered question from the database
def getNewQ():
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    sheet = db["new_question"]
    result = sheet.find()
    questionList = []
    for dict in result:
        questionDict = {}
        questionDict['question'] = dict['question']
        questionList.append(questionDict)
    client.close()
    return questionList

#delete the question who has been newly answered
def delQ(question):
    client = pymongo.MongoClient('localhost',27017)
    db = client["JD"]
    sheet = db["new_question"]
    #sheet.remove({"question":question},{"justOne":True})
    sheet.delete_one({"question":question})
    client.close()

if __name__ == '__main__':
    newQuestion("test")
    #delQ('test')
    info = getNewQ()
    print(info)