import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

train_data = pd.read_csv("./Data/transformed_train.csv", index_col=False, header=0)
test_data = pd.read_csv("./Data/transformed_test.csv", index_col=False, header=0)

X = train_data.iloc[:, :-1].values  # Input features
y = train_data.iloc[:, -1].values.reshape(-1, 1)

X_test = test_data.iloc[:, :].values

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X_test)

print(y_pred)
