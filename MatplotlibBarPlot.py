import matplotlib.pyplot as plt

def main():
    Langauage = ["C","CPP","Java","Python"]
    Students = [30,40,35,55]

    plt.bar(
        Langauage,             # values of x axis
        Students,              # values of y axis
        width = 0.6,           # width of bar
        edgecolor = "black",   # border color of bars
        linewidth = 1,         # width of bar border
        alpha = 0.8,           # Transperance 0.0 to 1.0 (Color)
        label = "Students"     # Legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Language")
    plt.ylabel("Number of Students")

    plt.grid(True)

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()