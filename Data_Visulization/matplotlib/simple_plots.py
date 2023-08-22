import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')


def square_numbers_plot():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    plt.tick_params(axis='both', labelsize=14)

    plt.show()


def square_numbers_scatter():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.inferno, edgecolors='none', s=40)

    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    plt.tick_params(axis="both", which="major", labelsize=14)

    plt.axis([0, 1100, 0, 1100000])

    plt.show()


def cubic_numbers_scatter():
    x_values = list(range(1, 1001))
    y_values = [x**3 for x in x_values]
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, edgecolors='none', s=50)

    plt.title('Cubic Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Cubic Value', fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.axis([0, 1100, 0, 1100000000])

    plt.show()


if __name__ == '__main__':
    square_numbers_plot()
    square_numbers_scatter()
    cubic_numbers_scatter()