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

if __name__ == '__main__':
    updateQA(4586850,"试试进去了么","进去了")
    info = getSellerQA(4586850)
    print(info)