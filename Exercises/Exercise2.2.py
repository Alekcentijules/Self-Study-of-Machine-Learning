import pandas as pd

df = pd.DataFrame({
    "Name":["Aleksandra", "Alex", "Brigitta", "Jagurdina"],
    "Age":[24, 22, 88, 53],
    "City":["Ukraine", "SiliconDoline", "Chikadritta", "Berdina"]
})

print(df[df["Age"] > 35])
print(df["Age"].mean())

df["Salary"] = [50000, 49993, 33333, 22222]

print(df)





