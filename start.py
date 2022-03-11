import time
import pygame
from data.colors import BLACK, WHITE, GREY, RED, GREEN, BLUE
from libs.objects import Ball
from libs.physics import Physics

FPS = 75
W, H = 1280, 720

surrounding = (0.3,  0.3)
acceleration = (0, 0)
ball1 = Ball('id1', 15, 50, GREY, Physics((300, 300), (200, 200), acceleration, surrounding))
ball2 = Ball('id2', 25, 150, WHITE, Physics((400, 300), (-200, 200), acceleration, surrounding))
ball3 = Ball('id3', 30, 250, RED, Physics((500, 100), (-200, -20), acceleration, surrounding))
ball4 = Ball('id4', 35, 350, GREEN, Physics((600, 50), (-300, 20), acceleration, surrounding))
ball5 = Ball('id5', 40, 450, BLUE, Physics((700, 100), (-400, 120), acceleration, surrounding))
balls = [ball1, ball2, ball3, ball4, ball5]


def physics(screen, dt):
    for num1, i in enumerate(balls):
        for num2, j in enumerate(balls):
            if num1 < num2:
                i.collide_with(j)
    for i in balls:
        i.update_ball(screen, dt)


def draw(screen):
    screen.fill(BLACK.color)
    for i in balls:
        i.draw_ball(screen)


def run():
    pygame.init()
    screen = pygame.display.set_mode((W, H))

    clock = pygame.time.Clock()
    time_last = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        dt = time.time() - time_last

        physics(screen, dt)
        draw(screen)
        pygame.display.flip()

        time_last = time.time()
        clock.tick(FPS)


def main():
    run()


if __name__ == '__main__':
    main()
