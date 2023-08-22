import pygal
import random

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

if __name__ == '__main__':
    die_1 = Die()
    die_2 = Die()

    results = [die_1.roll() + die_2.roll() for x in range(100000)]

    max_result = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(2, max_result + 1)]

    hist = pygal.Bar()

    hist.title = "Results of rolling two D6 dice 100000 times."
    hist.x_labels = list(map(str, range(2, max_result+1)))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6 + D6', frequencies)
    hist.render_to_file('dice_d6_d6_visual.svg')

