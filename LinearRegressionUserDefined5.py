import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables X :", X)
    print("Values of Dependent Variable Y :", Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is :", mean_x)
    print("Mean_Y is :", mean_y)

    n = len(X)   # 5

    numerator = 0
    denomenator = 0

    # formula :-> m = Sum(X-X_bar) * (Y-Y_bar) **2 / sum(X-X_bar)**2
    # Calculate slop i.e. m
    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denomenator = denomenator + ((X[i] - mean_x)**2)

    m = numerator / denomenator

    print("Slop of line :", m)

    # y = mx + c
    # c = y - mx
    # c = ymean - m * xmean

    c = mean_y - m * mean_x

    print("Y intercept is ie C:", c)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()