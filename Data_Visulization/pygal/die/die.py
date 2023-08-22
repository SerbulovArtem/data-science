import pygal
import random

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

if __name__ == '__main__':
    die = Die()

    results = [die.roll() for x in range(1000)]

    frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

    hist = pygal.Bar()

    hist.title = "Results of rolling one D6 1000 times."
    hist.x_labels = list(map(str, range(1, die.num_sides + 1)))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6', frequencies)
    hist.render_to_file('die_d6_visual.svg')

