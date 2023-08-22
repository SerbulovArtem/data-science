from die import Die

import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for x in range(100000)]

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 100000 times."

hist.x_labels = list(map(str, range(3, max_result+1)))
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add("D6 + D6 + D6", frequencies)

hist.render_to_file("dice_d6_d6_d6_visual.svg")