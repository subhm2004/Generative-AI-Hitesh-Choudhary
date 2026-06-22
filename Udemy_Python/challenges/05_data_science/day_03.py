# =============================================================================
# FILE    : day_03.py
# TOPIC   : Linear Regression — Salary predict karna experience se
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 03
# =============================================================================
#
# Machine Learning ka pehla model! Experience (X) se Salary (y) predict karte hain.
# Linear Regression = ek straight line fit karta hai data par — simple lekin powerful.

import pandas as pd
import matplotlib.pyplot as plt  # Charts aur graphs banane ke liye
from sklearn.linear_model import LinearRegression  # sklearn = ML library

# load data set
# CSV file se data padho — same folder mein honi chahiye
data = pd.read_csv("experience_salary.csv")

# X = input features (hum kya jaante hain) — double brackets se DataFrame column
X = data[["YearsExperience"]]

# y = target (hum kya predict karna chahte hain) — Salary
y = data[["Salary"]]

# LinearRegression model ka object banao
model = LinearRegression()

# model.fit() = model ko data sikhao — "training" kehte hain isko
model.fit(X, y)

# Ab model se predictions lo — actual salary ke saath compare karne ke liye naya column
data["PredictedSalary"] = model.predict(X)

# coef_ = slope (line ki steepness) — har extra saal experience se kitni salary badhti hai
print("Model Coefficient (slope)", round(float(model.coef_[0]), 2))

# intercept_ = jab experience 0 ho tab base salary
print("Model INtercept (base salary)", round(float(model.intercept_), 2))

# Visualization — blue dots = actual data, red line = model ki prediction
plt.scatter(X, y, color="blue", label="Actual Data")           # Scatter plot — dots
plt.plot(X, data["PredictedSalary"], color="red", label="Regression line")  # Line
plt.xlabel("Years of experience")   # X-axis label
plt.ylabel("Salary")                # Y-axis label
plt.title("Salary vs Experience")   # Chart ka title
plt.legend()                        # Legend = color ka matlab batata hai
plt.grid(True)                      # Grid lines — padhna easy ho
plt.tight_layout()                  # Layout adjust — overlap na ho
plt.show()                          # Window mein chart dikhao
