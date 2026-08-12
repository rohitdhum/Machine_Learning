from sklearn.datasets import load_iris

def main():
    print("_" * 30)
    print("Iris Classification case study")
    print("_" * 30)

    Dataset = load_iris()
    print(Dataset)

if __name__ == "__main__":
    main()