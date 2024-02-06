import torch
from torch.utils.data import Dataset
import glob
import numpy as np
import pandas as pd

from Columns import Columns

maxs = np.zeros(2000)
mins = np.zeros(2000)


class SegmentationDataset(Dataset):

    def __init__(self, train=True):

        self.train = train
        dataset_path = "./Data/" + ("train.csv" if train else "test.csv")

        df = pd.read_csv(dataset_path)

        df = df.drop(df.columns[0], axis=1)

        self.col_ix = 0

        while self.col_ix < df.shape[1]:

            if self.is_numerical(df.iloc[:, self.col_ix][1:]):
                df = self.handle_numerical_column(df, self.col_ix)
            else:
                df = self.handle_non_numerical_column(df, self.col_ix)


        self.length = df.shape[1]

        if (train):
            df.to_csv("./Data/transformed_train.csv", index=False)
            self.train_data = df
        else:
            df.to_csv("./Data/transformed_test.csv", index=False)
            self.test_data = df


    def is_numerical(self, column):
        try:
            pd.to_numeric(column)
            return True
        except ValueError:
            return False

    def handle_non_numerical_column(self, df, column_ix):

        values = Columns.columns[df.columns[column_ix]].values

        hot_encoded = pd.DataFrame()

        nan_locations = pd.isna(df.iloc[:, column_ix])

        for value in values:
            hot_encoded[value+str(column_ix)] = df.iloc[:, column_ix] == value

        hot_encoded["nan" + str(column_ix)] = nan_locations

        df = pd.concat([df.iloc[:, :column_ix+1], hot_encoded, df.iloc[:, column_ix+1:]], axis=1)

        df = df.drop(df.columns[column_ix], axis=1)

        self.col_ix += hot_encoded.shape[1]

        return df

    def handle_numerical_column(self, df, column_ix):

        df.iloc[:, column_ix] = df.iloc[:, column_ix].fillna(0)
        df.iloc[:, column_ix] = self.normalize_column(df, column_ix)
        self.col_ix += 1
        return df

    def normalize_column(self, df, column_ix):

        if(self.train):
            min_val = np.min(df.iloc[:, column_ix])
            max_val = np.max(df.iloc[:, column_ix])
        else:
            min_val = mins[column_ix]
            max_val = maxs[column_ix]

        if not (min_val == 0 and max_val == 1):
            normalized_column = (df.iloc[:, column_ix] - min_val) / (max_val - min_val)

            if(self.train):
                mins[column_ix] = min_val
                maxs[column_ix] = max_val

            return normalized_column

        # already normalized
        else:
            return df.iloc[:, column_ix]

    def __len__(self):
        if(self.train):
            return len(self.train_data)
        else:
            return len(self.test_data)

    def __getitem__(self, idx):

        if (self.train):
            example = self.train_data.iloc[idx, :-1].values.astype(np.float32)
            output = self.train_data.iloc[idx, -1].astype(np.float32)
            return example, output
        else:
            return self.test_data.iloc[idx].values.astype(np.float32)
