# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from kaggle import api as kaggle_api

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
folder = dataiku.Folder('download')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
folder_path = folder.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
kaggle_api.dataset_list_files('avenn98/world-of-warcraft-demographics').files

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
kaggle_api.dataset_list_files('joniarroba/noshowappointments').files

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
kaggle_api.dataset_download_files('joniarroba/noshowappointments', folder_path, quiet= False)
