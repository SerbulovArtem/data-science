import matplotlib.pyplot as plt
import random

plt.switch_backend('TkAgg')

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self) -> int:
        return random.randint(1, self.num_sides)


if __name__ == "__main__":
    die_1 = Die()
    die_2 = Die()

    results = [die_1.roll() + die_2.roll() for x in range(100000)]

    max_result = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(2, max_result+1)]

    x_values = [x for x in range(2, max_result+1)]

    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.bar(x_values, frequencies)

    plt.title("Results of rolling two D6 dice 100000 times.", fontsize=24)

    plt.xlabel('Result', fontsize=14)
    plt.ylabel('Frequency of Result', fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.xticks(x_values)

    plt.grid(True)
    plt.show()
