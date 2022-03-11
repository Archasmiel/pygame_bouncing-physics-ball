import pygame
from libs.physics import Physics
from libs.types import Color


def add_list(arr1: list, arr2: list):
    res = []
    for num in range(len(arr1)):
        res.append(arr1[num] + arr2[num])
    return res


def mult_list(mult: float, arr: list):
    return [mult*elem for elem in arr]


class Ball:

    def __init__(self, ident: str, r: int, mass: float, color: Color, physics: Physics):
        self.ident = ident
        self.r = r
        self.mass = mass
        self.color = color.color
        self.physics = physics

    def collide_with(self, ball):
        if self.ident != ball.ident:
            v1 = pygame.math.Vector2(self.physics.x0, self.physics.y0)
            v2 = pygame.math.Vector2(ball.physics.x0, ball.physics.y0)
            dist = v1.distance_to(v2)

            if dist < (self.r + ball.r + 5):
                ma, mb, m = self.mass, ball.mass, self.mass + ball.mass
                vai = [self.physics.vx0, self.physics.vy0]
                vbi = [ball.physics.vx0, ball.physics.vy0]

                vaf = add_list(mult_list((ma - mb) / m, vai), mult_list(2 * mb / m, vbi))
                vbf = add_list(mult_list(2 * ma / m, vai), mult_list((mb - ma) / m, vbi))

                self.physics.vx0, self.physics.vy0 = vaf[0], vaf[1]
                ball.physics.vx0, ball.physics.vy0 = vbf[0], vbf[1]

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.color, (round(self.physics.x0), round(self.physics.y0)), self.r)
        pygame.draw.line(screen, (225, 225, 225), (self.physics.x0, self.physics.y0),
                         (self.physics.x0 + self.physics.vx0 / 10, self.physics.y0 + self.physics.vy0 / 10), 2)

    def update_ball(self, screen, dt):

        future = self.physics.gravity_predict(dt)

        if future.x0 < self.r or future.x0 > (screen.get_width() - self.r):
            self.physics.vx0 = -self.physics.vx0 * self.physics.kx
        else:
            if abs(self.physics.vx0) < 10 ** -8:
                self.physics.vx0 = 0
            self.physics.gravity_update_x(dt)

        if future.y0 < self.r or future.y0 > (screen.get_height() - self.r):
            self.physics.vy0 = -self.physics.vy0 * self.physics.ky
        else:
            if abs(self.physics.vy0) < 10 ** -8:
                self.physics.vy0 = 0
            self.physics.gravity_update_y(dt)
