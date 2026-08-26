import numpy as np
import pandas as pd
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1 : Load the Data

#----------------------------------------------------------
#  Function Name : LoadData
#  Description : Load the Data from CSV
#  Input :       Name of CSV File
#  Output :      Data frame
#  Author :      Rohit Navin Dhumal
#  Date :        16/08/2026
#----------------------------------------------------------
def LoadData(Filename):
    df = pd.read_csv(Filename)

    print("Dataset loaded Succussfully")
    print(df.head())

    return df

#----------------------------------------------------------
#  Function Name : Main
#  Description : Entry point function
#  Input :       None
#  Output :      None
#  Author :      Rohit Navin Dhumal
#  Date :        16/08/2026
#----------------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()