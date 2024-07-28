import numpy as np
import math


docs = ['Tôi thích học AI', 'AI là trí tuệ nhân tạo',
        'AGI là siêu trí tuệ nhân tạo']


def compute_unique(doc):
    words = doc.lower().split(' ')
    unique_word = {}
    for word in words:
        if word in unique_word:
            unique_word[word] += 1
        else:
            unique_word[word] = 1

    return unique_word


def compute_tf(doc):
    words = doc.lower().split(' ')
    unique_word = compute_unique(doc)
    tf = {}
    for token, count in unique_word.items():
        tf[token] = count/len(words)

    return tf


def compute_idf(docs):
    num_docs = len(docs)
    idf = {}
    all_tokens = set(
        [token for doc in docs for token in compute_unique(doc).keys()])
    for token in all_tokens:
        num_containers = sum(
            1 for doc in docs if token in compute_unique(doc).keys())
        idf[token] = math.log(num_docs / (1 + num_containers))

    return idf


def compute_tf_idf(tf, idf):
    tf_idf = {}
    for token, tf_value in tf.items():
        tf_idf[token] = round(tf_value * idf.get(token, 0), 4)

    return tf_idf


tfs = [compute_tf(doc) for doc in docs]
idf = compute_idf(docs)
tf_idfs = [compute_tf_idf(tf, idf) for tf in tfs]

for i, (tf, tf_idf) in enumerate(zip(tfs, tf_idfs)):
    print(f"Document {i+1}:")
    print(f"{tf_idf}")
    print("\n")
