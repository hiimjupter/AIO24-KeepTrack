import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vi_data_df = pd.read_csv(
    "/Users/jupternguyen/Projects/EXT10004_AIO24/Homework/AIO24-KeepTrack/M02_Week4/vi_text_retrieval.csv")


# Question 10
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()

context_embedded = tfidf_vectorizer.fit_transform(context)

print(round(context_embedded.toarray()[7][0], 2))


# Question 11
def tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    # lowercasing the question before encoding
    question = question.lower()

    query_embedded = tfidf_vectorizer.transform([question])

    cosine_scores = cosine_similarity(
        query_embedded, context_embedded).flatten()

    # Get top k cosine scores and their indices
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)

    return results


question_q11 = vi_data_df.iloc[0]['question']
results_q11 = tfidf_search(question_q11, tfidf_vectorizer,
                           context_embedded, top_d=5)
print(round(results_q11[0]['cosine_score'], 2))


# Question 12
def corr_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    # Lowercasing the question before encoding
    question = question.lower()

    query_embedded = tfidf_vectorizer.transform([question]).toarray()

    corr_scores = np.corrcoef(
        np.vstack([query_embedded, context_embedded.toarray()]))

    corr_scores = corr_scores[0][1:]

    # Get top k correlation scores and their indices
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)

    return results


question_q12 = vi_data_df.iloc[0]['question']
results_q12 = corr_search(question_q12, tfidf_vectorizer,
                          context_embedded, top_d=5)
print(round(results_q12[1]['corr_score'], 2))
