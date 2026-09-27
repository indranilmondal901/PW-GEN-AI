import pandas as pd

# ------------------------------------------------------------
# 1. Creating a Series
# ------------------------------------------------------------
scores = pd.Series([80, 72, 91, 65, 88])

print("\nPandas Series:")
print(scores)

# ------------------------------------------------------------
# 2. Creating a DataFrame
# ------------------------------------------------------------
data = {
    "name": ["Amit", "Priya", "Rahul", "Neha", "Arjun"],
    "age": [20, 21, 19, 22, 20],
    "score": [85, 92, 74, 88, 95],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# ------------------------------------------------------------
# 3. head() and tail()
# ------------------------------------------------------------
print("\nFirst rows:")
print(df.head(3))

print("\nLast rows:")
print(df.tail(2))

# ------------------------------------------------------------
# 4. shape
# ------------------------------------------------------------
print("\nShape:")
print(df.shape)

# ------------------------------------------------------------
# 5. columns
# ------------------------------------------------------------
print("\nColumns:")
print(df.columns)

# ------------------------------------------------------------
# 6. info()
# ------------------------------------------------------------
print("\nInfo:")
df.info()

# ------------------------------------------------------------
# 7. describe()
# ------------------------------------------------------------
print("\nStatistics:")
print(df.describe())

# ------------------------------------------------------------
# 8. Selecting a column
# ------------------------------------------------------------
print("\nScores:")
print(df["score"])

# ------------------------------------------------------------
# 9. Selecting multiple columns
# ------------------------------------------------------------
print("\nName and score:")
print(df[["name", "score"]])

# ------------------------------------------------------------
# 10. loc
# ------------------------------------------------------------
print("\nUsing loc:")
print(df.loc[0, "name"])

print(df.loc[0:2, ["name", "score"]])

# ------------------------------------------------------------
# 11. iloc
# ------------------------------------------------------------
print("\nUsing iloc:")
print(df.iloc[0, 0])

print(df.iloc[0:3, 0:3])

# ------------------------------------------------------------
# 12. Filtering
# ------------------------------------------------------------
high_scores = df[df["score"] >= 85]

print("\nStudents with score >= 85:")
print(high_scores)

mumbai_students = df[df["city"] == "Mumbai"]

print("\nMumbai students:")
print(mumbai_students)

# ------------------------------------------------------------
# 13. Sorting
# ------------------------------------------------------------
sorted_df = df.sort_values("score", ascending=False)

print("\nSorted by score:")
print(sorted_df)

# ------------------------------------------------------------
# 14. Adding a column
# ------------------------------------------------------------
df["passed"] = df["score"] >= 50

print("\nAdded passed column:")
print(df)

# ------------------------------------------------------------
# 15. Renaming columns
# ------------------------------------------------------------
renamed_df = df.rename(columns={"score": "python_score"})

print("\nRenamed column:")
print(renamed_df)

# ------------------------------------------------------------
# 16. Missing values
# ------------------------------------------------------------
df_missing = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [80, None, 90, None]
})

print("\nMissing values:")
print(df_missing.isnull())

print("\nMissing value count:")
print(df_missing.isnull().sum())

# ------------------------------------------------------------
# 17. fillna()
# ------------------------------------------------------------
filled_df = df_missing.copy()
filled_df["score"] = filled_df["score"].fillna(0)

print("\nAfter fillna:")
print(filled_df)

# ------------------------------------------------------------
# 18. dropna()
# ------------------------------------------------------------
dropped_df = df_missing.dropna()

print("\nAfter dropna:")
print(dropped_df)

# ------------------------------------------------------------
# 19. value_counts()
# ------------------------------------------------------------
print("\nCity counts:")
print(df["city"].value_counts())

# ------------------------------------------------------------
# 20. groupby()
# ------------------------------------------------------------
city_average = df.groupby("city")["score"].mean()

print("\nAverage score by city:")
print(city_average)

# ------------------------------------------------------------
# 21. apply()
# ------------------------------------------------------------
df["score_plus_5"] = df["score"].apply(lambda x: x + 5)

print("\nUsing apply:")
print(df[["name", "score", "score_plus_5"]])

# ------------------------------------------------------------
# 22. Reading and writing CSV
# ------------------------------------------------------------
# Uncomment these when you want to work with an actual CSV file.
#
# df = pd.read_csv("students.csv")
# df.to_csv("students_output.csv", index=False)