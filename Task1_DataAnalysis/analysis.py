import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")
print("🔹 Student Marks Data:")
print(df)

print("\n🔸 Average Marks:")
print(df[['Math', 'Science', 'English']].mean())

topper = df[df['Science'] == df['Science'].max()]
print("\n🏆 Science Topper:", topper['Name'].values[0])

df[['Math', 'Science', 'English']].mean().plot(kind='bar', color='skyblue')
plt.title("Average Marks per Subject")
plt.ylabel("Marks")
plt.xlabel("Subjects")
plt.tight_layout()
plt.show()

plt.scatter(df['Math'], df['Science'], color='green')
plt.title("Math vs Science Scores")
plt.xlabel("Math")
plt.ylabel("Science")
plt.grid(True)
plt.show()

corr = df[['Math', 'Science', 'English']].corr()
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.title("Correlation Between Subjects")
plt.show()
