import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


vi_data_df = pd.read_csv(
    "/Users/jupternguyen/Projects/EXT10004_AIO24/Homework/AIO24-KeepTrack/M02_Week4/vi_text_retrieval.csv")


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


# Test case
context = vi_data_df['text']
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(round(results[0]['cosine_score'], 2))
