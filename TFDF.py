import tensorflow as tf
import tensorflow_decision_forests as tfdf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def split_dataset(dataset, test_ratio=0.30):
    test_indices = np.random.rand(len(dataset)) < test_ratio
    return dataset[~test_indices], dataset[test_indices]


train_file_path = "./Data/train.csv"
dataset_df = pd.read_csv(train_file_path)

dataset_df = dataset_df.drop('Id', axis=1)
dataset_df.head(3)

train_ds_pd, valid_ds_pd = split_dataset(dataset_df)
print("{} examples in training, {} examples in testing.".format(len(train_ds_pd), len(valid_ds_pd)))

label = 'SalePrice'
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(
    train_ds_pd,
    label=label,
    task = tfdf.keras.Task.REGRESSION
)

valid_ds = tfdf.keras.pd_dataframe_to_tf_dataset(
    valid_ds_pd,
    label=label,
    task=tfdf.keras.Task.REGRESSION
)

rf = tfdf.keras.RandomForestModel(task = tfdf.keras.Task.REGRESSION)
rf.compile(metrics=["mse"]) # Optional, you can use this to include a list of eval metrics

rf.fit(x=train_ds)

test_file_path = "./Data/test.csv"
test_data = pd.read_csv(test_file_path)
ids = test_data.pop('Id')

test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(
    test_data,
    task = tfdf.keras.Task.REGRESSION
)

preds = rf.predict(test_ds)
output = pd.DataFrame({
    'Id': ids,
    'SalePrice': preds.squeeze()})

output.head()

a = rf.predict(test_ds)
df = pd.DataFrame(a)

k = 1459  # Assuming k is the number of rows in the DataFrame
index_values = np.arange(k)
df["Id"] = index_values

df.columns = ["SalePrice"]



df.to_csv('./Data/polyregression.csv', index=False)
df.head()











