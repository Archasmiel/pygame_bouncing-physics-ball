g = 9.81 * 100


class Physics:

    def __init__(self, coordinates: tuple, speed: tuple, acceleration: tuple, coefficient: tuple, friction: float):
        self.x, self.y = coordinates[0], coordinates[1]
        self.vx, self.vy = speed[0], speed[1]
        self.ax, self.ay = acceleration[0], acceleration[1] + g

        self.afrx, self.afry = 0, 0

        self.kx, self.ky = 1 - coefficient[0], 1 - coefficient[1]
        self.kfr = friction

    def gravity_update_x(self, dt):
        self.x += self.vx * dt + self.ax * (dt ** 2) / 2
        self.vx += (self.ax + self.afrx) * dt

    def gravity_update_y(self, dt):
        self.y += self.vy * dt + self.ay * (dt ** 2) / 2
        self.vy += (self.ay + self.afry) * dt

    def get_tuple(self):
        return (self.x, self.y), (self.vx, self.vy), (self.ax, self.ay), (self.afrx, self.afry)

