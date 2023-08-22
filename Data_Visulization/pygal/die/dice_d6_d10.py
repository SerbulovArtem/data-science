from die import Die

import pygal

if __name__ == '__main__':
    die_1 = Die()
    die_2 = Die(10)

    results = [die_1.roll() + die_2.roll() for x in range(50000)]

    max_result = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(2, max_result+1)]

    hist = pygal.Bar()

    hist.title = "Results of rolling a D6 and D10 50,000 times."
    hist.x_labels = list(map(str, range(2, max_result+1)))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6 + D10', frequencies)
    hist.render_to_file('dice_d6_d10_visual.svg')

