# =============================================================================
# FILE    : day_04.py
# TOPIC   : Salary Predictor Web App (Streamlit se interactive app)
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 04
# =============================================================================
#
# Day 03 ka model ab website jaisi app mein — user experience daale, salary mile!
# Streamlit = Python se jaldi web apps banane ki library (HTML/CSS likhne ki zaroorat nahi).

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st  # st = streamlit ka short alias

# Pehle wala CSV data load karo
data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(X, y)

# --- Streamlit UI shuru ---

# st.title() = page ka bada heading
st.title("Salary Predictor based on experience")
st.write("Enter your years of experience to predict your salary:")

# number_input = user number type kar sakta hai; min/max/step limits set hain
years_input = st.number_input("Years of experience", min_value=0.0, max_value=50.0, step=0.1)

# Agar user ne kuch value daali hai (0 nahi), prediction dikhao
if years_input:
    print(years_input)  # Terminal mein bhi print (debugging ke liye)

    # [[years_input]] = 2D array chahiye sklearn ko; [0] se single number nikalo
    predicted_salary = model.predict([[years_input]])[0]

    # st.success = green box mein result — achha feel!
    st.success(f"Estimated Salary: {predicted_salary}")

# Neeche regression chart bhi dikhao
st.subheader("Regression Line")

# fig, ax = matplotlib figure aur axes — Streamlit ko chart dikhane ke liye
fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Actual Data")
ax.plot(X, model.predict(X), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

# st.pyplot() = matplotlib chart ko Streamlit page par render karta hai
st.pyplot(fig)
