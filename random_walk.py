from random import choice

class RandomWalk:
    def __init__(self, num_points=5000) -> None:
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self) -> None:
        while len(self.x_values) < self.num_points:
            x_dir = choice([-1, 1])
            x_dis = 1
            x_step = x_dir * x_dis

            y_dir = choice([-1, 1])
            y_dis = 1
            y_step = y_dir * y_dis

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)