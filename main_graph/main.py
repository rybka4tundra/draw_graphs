import typing as tp
from math import sqrt
import random
import time

from drawlib.apis import *

WIDTH = 256
HEIGHT = 256
N = 10


#
# There is no two dots with same coordinates
#

def random_dots_lst(n=10) -> list[list[int]]:
    return [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(n)]


def distance(dot_1, dot_2):
    return sqrt((dot_1[0] - dot_2[0]) ** 2 + (dot_1[1] - dot_2[1]) ** 2)


def find_nearest_dot(dot: list[int], context: dict[str, tp.Any]) -> list[int]:
    dot_1 = dot
    dots = context['dots']
    min_dist = 257
    min_dist_dot = list()
    for dot_2 in dots:
        dist = distance(dot_1, dot_2)
        if dist == 0:
            continue
        elif dist < min_dist:
            min_dist = dist
            min_dist_dot = dot_2
    return min_dist_dot


def find_nearest_dot_that_not_visited(dot: list[int], context: dict[str, tp.Any], visited: list[list[int]]) -> list[
    int]:
    dot_1 = dot
    dots = context['dots']
    min_dist = 257
    min_dist_dot = list()
    for dot_2 in dots:
        if dot_2 in visited:
            continue
        dist = distance(dot_1, dot_2)
        if dist == 0:
            continue
        elif dist < min_dist:
            min_dist = dist
            min_dist_dot = dot_2
    return min_dist_dot


def scan_dots(context: dict[str, tp.Any]) -> None:
    dots_cnt = int(input())
    context['dots'] = [[int(coordinate) for coordinate in input().split()] for _ in range(dots_cnt)]
    return None


def draw_canvas(context) -> None:
    dots = context.get('dots', None)

    if dots:
        visited = []
        dot = dots[context['shift']]
        while True:
            if dot in visited:
                break
            visited.append(dot)
            #circle(tuple(dot), radius=2)
            nearest_dot = find_nearest_dot_that_not_visited(dot, context, visited)
            if not nearest_dot:
                break
            line(tuple(dot), tuple(nearest_dot))
            # circle(tuple(dot), radius=distance(dot, nearest_dot),
            #        style=ShapeStyle(
            #            fcolor=Colors.Transparent,  # Fill color set to transparent
            #            lcolor=Colors.Blue,  # Outline color (e.g., blue)
            #        ))
            dot = nearest_dot

    return None


if __name__ == '__main__':
    context = {}
    context['dots'] = random_dots_lst(N)

    dir_str = str(time.time())
    config(width=WIDTH, height=HEIGHT)
    for i in range(N):
        context['shift'] = i
        draw_canvas(context)
        save(dir_str + '/' + 'circle_' + str(time.time()) + '.png')
        #clear()
