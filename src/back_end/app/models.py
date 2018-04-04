import pymongo
import jieba
from gensim.models import Word2Vec
from pprint import pprint

client = pymongo.MongoClient('localhost',27017)
db = client["JD"]
collection = db["item_info"]

item_id = 5706771

info = collection.find({'item_id': item_id})[0]["item_info"]

model = Word2Vec.load("app/text_processor/wordvec.model")

