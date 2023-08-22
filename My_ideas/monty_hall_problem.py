import pygal
import random

class Random_door():
    def __init__(self):
        self.quantity = 3
        self.doors = []

    def random_fill(self):
        self.doors.clear()
        for i in range(self.quantity):
            self.doors.append(0)
        self.doors[random.choice([0, 1, 2])] = 1
        pass

    def random_switch_choice(self):
        choice = random.choice([0, 1, 2])
        for i in range(self.quantity):
            if i != choice and self.doors[i] != 1:
                reveal_choice = i
        final_choice = self.quantity - (reveal_choice + choice)
        if self.doors[final_choice] == 1:
            self.random_fill()
            return 1
        else:
            self.random_fill()
            return 0

    def random_not_switch_choice(self):
        choice = random.choice([0, 1, 2])
        if self.doors[choice] == 1:
            self.random_fill()
            return 1
        else:
            self.random_fill()
            return 0


rd = Random_door()

rd.random_fill()

num = 100000
results1 = [rd.random_switch_choice() for x in range(num)]
results2 = [rd.random_not_switch_choice() for x in range(num)]

frequencies1 = [results1.count(value) / num for value in range(2)]
frequencies2 = [results2.count(value) / num for value in range(2)]

chart = pygal.Bar()

chart.title = 'Monty Hall problem'

chart.x_labels= ['Lose', 'Win']
chart.x_title = 'Lose/Win case'
chart.y_title = 'Probability'

chart.add("Switch choice", frequencies1)
chart.add("Not switch choice", frequencies2)

chart.render_to_file('monty_hall_problem_visual.svg')