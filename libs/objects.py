from math import radians, cos, sin, atan

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

    @staticmethod
    def equalify(coord1, coord2, ineq, trig):
        if coord1 > coord2:
            coord1 += ineq * trig / 2
            coord2 -= ineq * trig / 2
        else:
            coord1 -= ineq * trig / 2
            coord2 += ineq * trig / 2

    def collide_with(self, ball):
        if self.ident != ball.ident:
            v1 = pygame.math.Vector2(self.physics.x0, self.physics.y0)
            v2 = pygame.math.Vector2(ball.physics.x0, ball.physics.y0)
            dist = v1.distance_to(v2)
            angle = atan(v2.y-v1.y/v2.x-v1.x)

            if dist < (self.r + ball.r):

                inequality = self.r + ball.r - dist
                self.equalify(self.physics.x0, ball.physics.x0, inequality, cos(angle))
                self.equalify(self.physics.y0, ball.physics.y0, inequality, sin(angle))

                ma, mb, m = self.mass, ball.mass, self.mass + ball.mass
                vai = [self.physics.vx0, self.physics.vy0]
                vbi = [ball.physics.vx0, ball.physics.vy0]

                vaf = add_list(mult_list((ma - mb) / m, vai), mult_list(2 * mb / m, vbi))
                vbf = add_list(mult_list(2 * ma / m, vai), mult_list((mb - ma) / m, vbi))

                self.physics.vx0, self.physics.vy0 = vaf[0], vaf[1]
                ball.physics.vx0, ball.physics.vy0 = vbf[0], vbf[1]

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.color, (round(self.physics.x0), round(self.physics.y0)), self.r)
        pygame.draw.circle(screen, (128, 128, 0), (round(self.physics.x0), round(self.physics.y0)), self.r, 1)
        pygame.draw.line(screen, (225, 225, 225), (self.physics.x0, self.physics.y0),
                         (self.physics.x0 + self.physics.vx0 / 10, self.physics.y0 + self.physics.vy0 / 10), 2)

    def update_ball(self, screen, dt):

        self.physics.gravity_update_x(dt)
        if abs(self.physics.vx0) < 10 ** -8:
            self.physics.vx0 = 0
        if self.physics.x0 < self.r:
            self.physics.vx0 = -self.physics.vx0 * self.physics.kx
            self.physics.x0 = self.r
        elif self.physics.x0 > (screen.get_width() - self.r):
            self.physics.vx0 = -self.physics.vx0 * self.physics.kx
            self.physics.x0 = screen.get_width() - self.r

        self.physics.gravity_update_y(dt)
        if abs(self.physics.vy0) < 10 ** -8:
            self.physics.vy0 = 0
        if self.physics.y0 < self.r:
            self.physics.vy0 = -self.physics.vy0 * self.physics.ky
            self.physics.y0 = self.r
        elif self.physics.y0 > (screen.get_height() - self.r):
            self.physics.vy0 = -self.physics.vy0 * self.physics.ky
            self.physics.y0 = screen.get_height() - self.r
