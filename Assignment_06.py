import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Chocolate Sales (2).csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.columns)
print(df.loc[2])
print(df.iloc[-1])
subset=df[['Country', 'Product']]
print(subset.head())
print(df.max())
print(df.min())
print(df.mean(numeric_only = True))
print(df.median(numeric_only = True))
print(df.mode())
print(df.std(numeric_only = True))
print(df.var(numeric_only = True))
print(df.skew(numeric_only = True))

plt.plot(df['Amount'], df["Country"])
plt.xlabel("Amount")
plt.ylabel("Country")
plt.title("Line graph")
plt.show()

df["Amount"].value_counts().plot(kind="bar")
plt.show()

plt.scatter(df["Amount"], df["Country"])
plt.show()

plt.hist(df["Amount"], bins = 10)
plt.show()

plt.boxplot(df["Amount"])
plt.show()

df["Amount"] = df["Amount"].replace('[\$,]', ' ', regex = True)
df["Amount"] = pd.to_numeric(df["Amount"], errors = 'coerce')