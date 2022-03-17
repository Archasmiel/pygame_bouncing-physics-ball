from math import cos, sin, atan

import pygame
from libs.physics import Physics
from libs.types import Color

g = 9.81 * 100


def add_list(arr1: list, arr2: list):
    res = []
    for num in range(len(arr1)):
        res.append(arr1[num] + arr2[num])
    return res


def mult_list(mult: float, arr: list):
    return [mult * elem for elem in arr]


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
            coord1 += ineq * trig / 2 + 1.5
            coord2 -= ineq * trig / 2 + 1.5
        else:
            coord1 -= ineq * trig / 2 + 1.5
            coord2 += ineq * trig / 2 + 1.5
        return coord1, coord2

    @staticmethod
    def check_bounds(coord, coord_check, bound):
        return coord_check - bound < coord < coord_check + bound

    @staticmethod
    def update_coordinates(coord, speed, mini, maxi, k):
        if abs(speed) < 10 ** -8:
            speed = 0
        if coord < mini:
            speed *= -k
            coord = mini
        elif coord > maxi:
            speed *= -k
            coord = maxi
        return coord, speed

    def normalizing_balls(self, ball, v1, v2, dist):
        angle = atan(v2.y - v1.y / v2.x - v1.x)
        inequality = self.r + ball.r - dist
        self.physics.x, ball.physics.x = self.equalify(self.physics.x, ball.physics.x,
                                                       inequality, cos(angle))
        self.physics.y, ball.physics.y = self.equalify(self.physics.y, ball.physics.y,
                                                       inequality, sin(angle))

    def collide_with(self, ball):
        if self.ident != ball.ident:
            v1 = pygame.math.Vector2(self.physics.x, self.physics.y)
            v2 = pygame.math.Vector2(ball.physics.x, ball.physics.y)
            dist = v1.distance_to(v2)

            if dist < (self.r + ball.r):
                self.normalizing_balls(ball, v1, v2, dist)

                ma, mb, m = self.mass, ball.mass, self.mass + ball.mass
                vai = [self.physics.vx, self.physics.vy]
                vbi = [ball.physics.vx, ball.physics.vy]

                vaf = add_list(mult_list((ma - mb) / m, vai), mult_list(2 * mb / m, vbi))
                vbf = add_list(mult_list(2 * ma / m, vai), mult_list((mb - ma) / m, vbi))

                self.physics.vx, self.physics.vy = vaf[0], vaf[1]
                ball.physics.vx, ball.physics.vy = vbf[0], vbf[1]

    def update_friction(self, screen):
        speed_mod = (self.physics.vx**2 + self.physics.vy**2) ** 0.5
        speed_rvect = self.physics.vx/speed_mod, self.physics.vy/speed_mod
        if self.check_bounds(self.physics.x, self.r, 1) or \
                self.check_bounds(self.physics.x, screen.get_width() - self.r, 1):
            self.physics.afry = -speed_rvect[1] * g * self.physics.kfr
        else:
            self.physics.afrx = 0

        if self.check_bounds(self.physics.y, self.r, 1) or \
                self.check_bounds(self.physics.y, screen.get_height() - self.r, 1):
            self.physics.afrx = -speed_rvect[0] * g * self.physics.kfr
        else:
            self.physics.afry = 0

    def update_ball(self, screen, dt):

        self.physics.gravity_update_x(dt)
        self.physics.x, self.physics.vx = self.update_coordinates(self.physics.x, self.physics.vx, self.r,
                                                                  screen.get_width() - self.r, self.physics.kx)

        self.physics.gravity_update_y(dt)
        self.physics.y, self.physics.vy = self.update_coordinates(self.physics.y, self.physics.vy, self.r,
                                                                  screen.get_height() - self.r, self.physics.ky)

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.color, (round(self.physics.x), round(self.physics.y)), self.r)
        pygame.draw.circle(screen, (128, 12, 0), (round(self.physics.x), round(self.physics.y)), self.r, 2)
        pygame.draw.line(screen, (225, 225, 225), (self.physics.x, self.physics.y),
                         (self.physics.x + self.physics.vx / 10, self.physics.y + self.physics.vy / 10), 2)




