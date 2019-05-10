#encoding=utf-8

import jieba
import codecs
import os


class zhcnSeg(object):
    stopwords = []
    current_path = os.path.dirname(__file__)
    stopword_filepath = current_path+"/stopword.txt"


    def __init__(self):
        self.read_in_stopword()

    def read_in_stopword(self):
        file_obj = codecs.open(self.stopword_filepath,'r','utf-8')
        while True:
            line = file_obj.readline()
            line=line.strip('\r\n')
            if not line:
                break
            self.stopwords.append(line)
        file_obj.close()

    # jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
    def cut(self,sentence,stopword=True):
        seg_list = jieba.cut(sentence)

        results = []
        for seg in seg_list:
            if seg in self.stopwords and stopword:
                continue
            results.append(seg)

        return results

    # jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
    def cut_for_search(self,sentence,stopword=True):
        seg_list = jieba.cut_for_search(sentence)

        results = []
        for seg in seg_list:
            if seg in self.stopwords and stopword:
                continue
            results.append(seg)

        return results
