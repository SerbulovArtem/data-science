import random
import pygal
from pygal.style import Style

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        return random.choice([1, -1]) * random.choice(list(range(9)))


def chart_xy_random_walk():
    rw = RandomWalk(5000)
    rw.fill_walk()

    custom_style = Style(colors=('#0000ff', '#00ff00', '#ff0000'))

    chart_XY = pygal.XY(stroke=False, show_x_labels=False, show_y_labels=False, style=custom_style)

    chart_XY.title = "Random Walk"

    result = list(zip(rw.x_values, rw.y_values))
    chart_XY.add("RW", result)
    chart_XY.add("Begin", [(0, 0)])
    chart_XY.add("End", [(rw.x_values[-1], rw.y_values[-1])])

    chart_XY.render_to_file("chart_xy_random_walk_visual.svg")


def line_random_walk():
    rw = RandomWalk(5000)
    rw.fill_walk()

    custom_style = Style(colors=('#0000ff', '#00ff00', '#ff0000'))

    chart_XY = pygal.XY(stroke=True, show_dots=True, show_x_labels=False, show_y_labels=False, style=custom_style)

    chart_XY.title = "Random Walk"

    result = list(zip(rw.x_values, rw.y_values))
    chart_XY.add("RW", result)

    chart_XY.add("Begin", [(0, 0)])
    chart_XY.add("End", [(rw.x_values[-1], rw.y_values[-1])])

    chart_XY.render_to_file("line_random_walk_visual.svg")


if __name__ == "__main__":
    chart_xy_random_walk()
    line_random_walk()
    pass
