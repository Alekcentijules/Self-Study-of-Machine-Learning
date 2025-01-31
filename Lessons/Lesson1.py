# NumPy

import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__, '\n')


array = np.array([1, 2, 3, 4, 5, 6])
print(f"np.array - {array}\n")


array1 = np.arange(1, 22, 2)
array2 = np.arange(1, 10, 3)
print(f"np.arange1 - {array1}")
print(f"np.arange2 - {array2}\n")

rand_array = np.random.randint(1, 22, size=10)
print(f"np.random.randint - {rand_array}\n")

array2_tiled = np.tile(array2, 4)[:len(array1)]
print(f"np.tile - {array2_tiled}")

pl_array = array1 + array2_tiled
print(f"plus array - {pl_array}")


mean_ = np.mean(pl_array)
max_ = np.max(pl_array)
min_ = np.min(pl_array)
print(f"np.mean - {mean_}")
print(f"np.max - {max_}")
print(f"np.min - {min_}\n")



# Pandas

series = pd.Series([1, 2, 3, 4, 5, 6])
print("pd.Series -")
print(series, '\n')


data = {"Name": ["Franklin", "Jango", "Bob", "ShelvineShlain"], "Age": [45, 34, 72, 777]}
df = pd.DataFrame(data)
print("pd.DataFrame -")
print(df, '\n')


# df = pd.read_csv("data.csv")
# print(df)


print("df[df['Age'] < 40] -")
print(df[df['Age'] < 40], '\n')

print("df['Age'].mean -")
print(df['Age'].mean(), '\n')

print('df["Age"].max(), df["Age"].min() -')
print(df["Age"].max(), df["Age"].min())
