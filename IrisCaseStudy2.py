from sklearn.datasets import load_iris

def main():
    print("_" * 30)
    print("Iris Classification case study")
    print("_" * 30)

    Dataset = load_iris()

    # MetaData of dataset
    print("Independent varibles are :")
    print(Dataset.feature_names)

    print("Dependent variables are :")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()