g = 9.81 * 100


class Physics:

    def __init__(self, coordinates: tuple, speed: tuple, acceleration: tuple, coefficient: tuple):
        self.x0, self.y0 = coordinates[0], coordinates[1]
        self.vx0, self.vy0 = speed[0], speed[1]
        self.ax0, self.ay0 = acceleration[0], acceleration[1] + g
        self.kx, self.ky = 1 - coefficient[0], 1 - coefficient[1]

    def gravity_update_x(self, dt):
        self.x0 += self.vx0 * dt + self.ax0 * (dt ** 2) / 2
        self.vx0 += self.ax0 * dt

    def gravity_update_y(self, dt):
        self.y0 += self.vy0 * dt + self.ay0 * (dt ** 2) / 2
        self.vy0 += self.ay0 * dt

    def get_tuple(self):
        return (self.x0, self.y0), (self.vx0, self.vy0), (self.ax0, self.ay0)

