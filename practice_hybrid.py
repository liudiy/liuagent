from rank_bm25 import BM25Okapi
import jieba

corpus = [
   "苹果",
   "橙子",
   "香蕉"
]

tokenized_corpus = [doc.split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)
# <rank_bm25.BM25Okapi at 0x1047881d0>


query = "windy London"
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)

print(doc_scores)
# array([0.        , 0.93729472, 0.        ])