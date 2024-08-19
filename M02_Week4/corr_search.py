import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


vi_data_df = pd.read_csv(
    "/Users/jupternguyen/Projects/EXT10004_AIO24/Homework/AIO24-KeepTrack/M02_Week4/vi_text_retrieval.csv")


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


# Test case
context = vi_data_df['text']
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(round(results[1]['corr_score'], 2))
