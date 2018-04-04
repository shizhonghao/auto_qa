from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from pprint import pprint
import jieba

def train():
    pass

clf = svm.SVC(kernel = 'linear')
with open("similarity_out.txt","r") as f:
    sentence = []
    lable = []
    for line in f:
        #line = line.split()
        lable.append(int(line[0]))
        questionList = jieba.cut(line[2:-1])
        question_seg = " ".join(questionList)
        sentence.append(question_seg)

    #pprint(sentence)
    count_vec = CountVectorizer()
    count_train = count_vec.fit_transform(sentence[:-10])
    
    count_vec_2 = CountVectorizer(vocabulary = count_vec.vocabulary_)
    count_test = count_vec_2.fit_transform(sentence[-10:])
    print(count_train.shape, count_test.shape)

    tfidf_trans = TfidfTransformer()
    tfidf_train = tfidf_trans.fit(count_train).transform(count_train)
    tfidf_test = tfidf_trans.fit(count_test).transform(count_test)
    
    #print(tfidf_train)
    clf.fit(tfidf_train,lable[:-10])

    result = clf.predict(tfidf_test)
    print(result)

# 
def is_KB_QA(s):
    print(type(s))
    print(type(sentence[-1]))
    count_vec_2 = CountVectorizer(vocabulary = count_vec.vocabulary_)
    count_test = count_vec_2.fit_transform([s])
    tfidf_test = tfidf_trans.fit(count_test).transform(count_test)
    result = clf.predict(tfidf_test)
    print(result)
    pass

if __name__ == "__main__":
    x = ["有","分屏","功能","吗","？"]
    s = " ".join(x)
    print(s)
    is_KB_QA(s)
