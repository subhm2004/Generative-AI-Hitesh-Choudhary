# =============================================================================
# FILE    : day_10.py
# TOPIC   : Book Recommendation Web App (Streamlit + Cosine Similarity)
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 10
# =============================================================================
#
# Day 09 ka recommendation logic ab Streamlit app mein —
# user book title likhe, similar books ki table dikhe!

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Books data load karo
df = pd.read_csv("books.csv")

# Data clean karo — extra spaces hatao, missing description ko khali string se bharo
df['title'] = df['title'].str.strip()
df['description'] = df['description'].fillna("")

# TF-IDF vectors aur similarity matrix banao (day_09 jaisa)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Title lookup — lowercase + duplicate titles handle (drop_duplicates)
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()


def get_recommendations(title, df,  cosine_sim, indices):
    """
    User ke diye title ke liye recommendations return karta hai.
    Book nahi mili toh error message string return hota hai.
    """
    # User input ko normalize karo — spaces + lowercase
    title = title.strip().lower()

    # Agar title dataset mein nahi hai
    if title not in indices.index:
        return f"{title} not found in dataset"

    # Book ka index nikalo
    idx = indices.loc[title]

    # Kabhi-kabhi duplicate titles ki wajah se Series aata hai — pehla index lo
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]


    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]


# --- Streamlit UI ---

st.title("Book Recommendation Engine")
st.write("Enter a book title and get similar recommendation")

# User se book title input lo
select_book = st.text_input("Book: Title")

if select_book:
    # Recommendations function call karo
    results = get_recommendations(select_book, df, cosine_sim, indices)

    # Agar DataFrame mila = books mili — table dikhao
    if isinstance(results, pd.DataFrame):
        st.table(results)
    else:
        # String mila = error message (book not found)
        st.warning(results)
