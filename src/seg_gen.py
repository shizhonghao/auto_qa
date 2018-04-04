import jieba

with open(r'C:\Users\施中昊\Desktop\2017 coding\jd_scrapy\sentence.txt','r') as f:
    with open(r'C:\Users\施中昊\Desktop\实验室\auto_qa\segmentation.txt','a') as w:
        for line in f:
            line.replace('\t', '').replace(' ','')#.replace('\n', '')
            seg_list = jieba.cut(line)
            w.write(" ".join(seg_list))
