import matplotlib.pyplot as plt
import random

plt.switch_backend('TkAgg')


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


def scatter_random_walk():
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.axis('off')

    plt.show()


def molecular_motion_random_walk():
    rw = RandomWalk()
    rw.fill_walk()

    #px = 1 / plt.rcParams['figure.dpi']
    #plt.figure(figsize=(1920 * px, 1080 * px))

    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)

    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    plt.axis('off')

    plt.show()


if __name__ == '__main__':
    while True:
        scatter_random_walk()
        molecular_motion_random_walk()
        keep_running = input('Make another walk? (y/n): ')
        if keep_running == 'n':
            break