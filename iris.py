import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, log_loss
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.tree import DecisionTreeClassifier


plt.rcParams.update({"figure.constrained_layout.use": True})

iris = pd.read_csv(
    "https://gist.githubusercontent.com"
    "/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
).rename(columns=lambda c: c.replace(".", "_"))
iris.to_csv("iris.csv", index=False)
del iris

iris = pd.read_csv("iris.csv")
iris_2 = pd.DataFrame(
    {
        "sepal_length": [5.94, 5.87],
        "sepal_width": [2.7, 3.21],
        "petal_length": [5.12, 4.99],
        "petal_width": [1.81, 1.77],
        "variety": ["Virginica", "Virginica"],
    },
    index=[150, 151],
)
iris = pd.concat((iris, iris_2))
iris
