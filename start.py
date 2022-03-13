import math
import time
import pygame
from data.colors import BLACK, WHITE, GREY, RED, GREEN, BLUE
from libs.objects import Ball
from libs.physics import Physics

UPDATING = 5
FPS = 100
W, H = 1280, 720

surrounding = (0.2,  0.2)
acceleration = (0, 0)
friction = 0.1
ball1 = Ball('id1', 30, 10, GREY, Physics((20, H-20), (200, 0), acceleration, surrounding, friction))
ball2 = Ball('id2', 40, 10, WHITE, Physics((W-40, H-40), (-200, 0), acceleration, surrounding, friction))
ball3 = Ball('id3', 30, 250, RED, Physics((500, 100), (-200, -20), acceleration, surrounding, friction))
ball4 = Ball('id4', 35, 350, GREEN, Physics((600, 50), (-300, 20), acceleration, surrounding, friction))
ball5 = Ball('id5', 40, 450, BLUE, Physics((700, 100), (-400, 120), acceleration, surrounding, friction))
balls = [ball1, ball2, ball3, ball4, ball5]


def physics(screen, dt):
    for _ in range(UPDATING):
        for num1, i in enumerate(balls):
            for num2, j in enumerate(balls):
                if num1 < num2:
                    i.collide_with(j)
        for i in balls:
            i.update_friction(screen)
            # if i.ident == 'id1':
            #     print(i.physics.get_tuple())
            i.update_ball(screen, dt/UPDATING)


def draw(screen):
    screen.fill(BLACK.color)
    for i in balls:
        i.draw_ball(screen)
    pygame.draw.line(screen, RED.color, (W//2+10*math.cos(-math.pi/2), H//2+10*math.sin(-math.pi/2)),
                     (W//2+10*math.cos(math.pi/2), H//2+10*math.sin(math.pi/2)))
    pygame.draw.line(screen, RED.color, (W//2+10*math.cos(0), H//2+10*math.sin(0)),
                     (W//2+10*math.cos(math.pi), H//2+10*math.sin(math.pi)))
    pygame.display.flip()


def run():
    pygame.init()
    screen = pygame.display.set_mode((W, H))

    clock = pygame.time.Clock()
    time_last = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        clock.tick(FPS)
        dt = time.time() - time_last

        physics(screen, dt)
        draw(screen)

        time_last = time.time()


def main():
    run()


if __name__ == '__main__':
    main()
