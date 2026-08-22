import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def marvellousClassifier(DataPath):
    border = "-" * 40

    # Step 1: Load the dataset from csv file
    print(border)
    print("Step 1: Load the dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset :")
    print(df.head())
    print(border)

    # Step 2: Clean the dataset
    print(border)
    print("Step 2 : Clean the dataset")
    print(border)

    df.dropna(inplace=True)

    print("Shape of dataset :", df.shape)
    print("Total Records :", df.shape[0])
    print("Total columns :", df.shape[1])

    # Step 3: separate Independent and Dependent variables
    print(border)
    print("Step 3: separate Independent and Dependent variables")
    print(border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X :", X.shape)
    print("Shape of X :", Y.shape)

    print(border)
    print("Input columns :", X.columns.tolist())
    print("Output column : Class")
    print(border)

    # Step 4: Split the dataset for training and testing
    print(border)
    print("Step 4: Split the dataset for training and testing")
    print(border)

    X_test, X_train, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Details of traing and testing data")

    print("Shape of X_train :", X_train.shape)
    print("Shape of X_test :", X_test.shape)

    print("Shape of Y_train :", Y_train.shape)
    print("Shape of Y_test :", Y_test.shape)

    print(border)

    # Step 5: Feature Scalling
    print(border)
    print("Step 5: Feature Scalling")
    print(border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Featre scaling done")

    print(border)

def main():
    marvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()