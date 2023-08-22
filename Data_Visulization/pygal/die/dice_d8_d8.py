from die import Die

import pygal

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for x in range(100000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 100000 times."

hist.x_labels = list(map(str, range(2, max_result+1)))
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add("D8 + D8", frequencies)

hist.render_to_file("dice_d8_d8_visual.svg")