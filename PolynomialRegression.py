import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

train_data = pd.read_csv("./Data/transformed_train.csv", index_col=False, header=0)
test_data = pd.read_csv("./Data/transformed_test.csv", index_col=False, header=0)

X = train_data.iloc[:, :-1].values  # Input features
y = train_data.iloc[:, -1].values.reshape(-1, 1)

X_test = test_data.iloc[:, :].values

degree = 2  # Set the degree of the polynomial
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

X_test_poly = poly_features.transform(X_test)

y_pred = model.predict(X_test_poly)

print(y_pred)
