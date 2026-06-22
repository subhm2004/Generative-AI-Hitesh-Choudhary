# =============================================================================
# FILE    : day_02.py
# TOPIC   : Fake Salary Dataset Banana (Experience vs Salary data generate karna)
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 02
# =============================================================================
#
# Yeh script machine learning ke liye sample data banati hai —
# kitne saal experience hai aur kitni salary hai, 100 rows ka CSV file.
# NumPy = numbers ke saath fast kaam; Pandas = tables (DataFrame) ke saath kaam.

# numpy — numerical arrays aur random numbers ke liye (short name: np)
import numpy as np

# pandas — Excel jaisi tables handle karta hai (short name: pd)
import pandas as pd

# random seed fix karo taaki har baar same random numbers aayein (reproducible results)
# 42 ek popular choice hai programmers mein 😄
np.random.seed(42)

# 100 random experience values — 0.5 se 10 saal ke beech
# uniform = har value equally likely; round(2) = 2 decimal places
years = np.random.uniform(0.5, 10, 100).round(2)

# Salary formula: base 30000 + har saal ke liye 6000 + thoda random noise
# normal(0, 4000) = realistic variation ke liye randomness
salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100) ).round(2)

# DataFrame = table jisme columns hain — Excel sheet jaisa
df = pd.DataFrame({
    "YearsExperience": years,   # Pehla column
    "Salary": salaries          # Doosra column
})

# CSV file mein save karo; index=False matlab row numbers file mein mat likho
df.to_csv("experience_salary.csv", index=False)
print("Data saved in file ✅")
