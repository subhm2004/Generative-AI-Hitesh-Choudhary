# =============================================================================
# FILE    : day_06.py
# TOPIC   : Text Classification — Toxic vs Supportive comment detect karna
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 06
# =============================================================================
#
# Machine Learning se text samajhna — comment toxic hai ya supportive?
# Pipeline = multiple steps ek saath (text → numbers → model).
# TF-IDF = words ko numbers mein badalta hai; Logistic Regression = classify karta hai.

import pandas as pd
from sklearn.pipeline import Pipeline  # Steps ko chain karna
from sklearn.linear_model import LogisticRegression  # Classification algorithm
from sklearn.feature_extraction.text import TfidfVectorizer  # Text → numerical vectors
from sklearn.model_selection import train_test_split  # Data ko train/test mein baantna

# Day 05 ki CSV file load karo
df = pd.read_csv("youtube_comments.csv")

# Data ko 80% training, 20% testing mein split karo
# random_state=42 = har baar same split (reproducible)
# X = comments (text), y = labels (toxic/support)
X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['label'], test_size=0.2, random_state=42)

# Pipeline — pehle TF-IDF, phir Logistic Regression; ek saath fit/predict
model = Pipeline([
    ('tfidf', TfidfVectorizer()),      # Step 1: text ko numbers mein badlo
    ('clf', LogisticRegression())      # Step 2: classify karo
])

# Sirf training data par model sikhayo — test data abhi chhupa hai!
model.fit(X_train, y_train)

# model.score() = test set par kitne % sahi predict hue
acc = model.score(X_test, y_test)
print(f"Model tained. Accuracy: {round(acc * 100, 2)}%")
