# =============================================================================
# FILE    : day_07.py
# TOPIC   : YouTube Comment Classifier App (Streamlit web interface)
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 07
# =============================================================================
#
# Day 06 ka trained model ab user-friendly app mein —
# user comment likhe, app bataye toxic hai ya supportive!

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import streamlit as st


# @st.cache_resource = model sirf ek baar load/train hoga, har refresh par nahi
# Decorator = function ke upar @ — behavior change karta hai bina andar code badle
@st.cache_resource
def load_model():
    """
    CSV se data padhkar model train karta hai aur return karta hai.
    Cache ki wajah se app fast rehti hai — dubara train nahi hota.
    """
    df = pd.read_csv("youtube_comments.csv")
    model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
    ])
    # Poora data par train — simple demo app ke liye OK
    model.fit(df['comment'], df['label'])
    return model


# App start hote hi model load karo
model = load_model()

st.title("Youtube comment classifier")
st.write("Classify your comment as Toxic or supportive")

# text_area = bada text box — user apna comment likh sakta hai
user_input = st.text_area("Enter a youtube comment")

# Jab user ne kuch likha ho tab hi predict karo
if user_input:
    # predict() list of texts leta hai — [user_input] = ek comment ki list
    # [0] = pehla (aur akela) result
    prediction = model.predict([user_input])[0]

    if prediction == "toxic":
        # st.error = red warning style — toxic comment ke liye
        st.error("This comment is likely **Toxic**")
    else:
        # st.success = green — supportive comment
        st.success("This comment is **Supportive**")

