# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
data_train = dataiku.Dataset('data_train')

train_df = data_train.get_dataframe()
data_eval = dataiku.Dataset("data_eval")
eval_df = data_eval.get_dataframe()

# Write recipe outputs
data_folder = dataiku.Folder('data').get_path()

train_df.to_csv(data_folder + '/train.csv', index= False)

eval_df.to_csv(data_folder  + '/eval.csv', index= False)