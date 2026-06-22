# =============================================================================
# FILE    : day_09.py
# TOPIC   : Book Recommendation Engine (Cosine Similarity se similar books)
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 09
# =============================================================================
#
# Agar aapko ek book pasand hai, similar books suggest karte hain!
# TF-IDF se description ko numbers banate hain; cosine similarity se
# kitni "similar" hain woh measure karte hain (0 se 1, 1 = bilkul same).

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  # Do vectors kitne similar hain


# books.csv se saari books load karo
df = pd.read_csv("books.csv")

# TfidfVectorizer — book descriptions ko numerical vectors mein badalta hai
# stop_words='english' = "the", "is", "a" jaisi common words ignore karo
vectorizer = TfidfVectorizer(stop_words='english')

# fit_transform = seekho + transform — har book ka TF-IDF vector
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Har book vs har book similarity matrix — square matrix (10x10 for 10 books)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Title se index dhundhne ke liye — book naam → row number
indices = pd.Series(df.index, index=df['title'])


def get_recommendations(title, cosine_sim=cosine_sim):
    """
    Diye gaye book title ke liye top 5 similar books return karta hai.
    title = user ne jo book naam diya
    cosine_sim = similarity matrix (default same file wali)
    """
    # Book ka row index nikalo
    idx = indices[title]

    # Is book ki sab books ke saath similarity scores — enumerate se (index, score) pairs
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Score ke hisaab se sort karo, highest pehle; [1:6] = khud ko chhod kar top 5
    # [0] khud ki book hai (100% similar) — usko skip karte hain
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    # Sirf book indices nikalo (scores nahi chahiye ab)
    book_indices = [i[0] for i in sim_scores]

    # Un rows se title aur author columns return karo
    return df[['title', 'author']].iloc[book_indices]
