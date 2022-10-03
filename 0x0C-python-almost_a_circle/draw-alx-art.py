#!/usr/bin/python3
"""Module draw-alx-art

This Module contains a script to generate an ALX colorful art
"""
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":
    list_rectangles = []
    list_squares = []

    width = 20
    height = 30

    # Letter A
    x_coords = [x for x in range(0, width * 9, width)]
    y_coords = (
        [y for y in range(height, height * 6, height)] +
        [y for y in range(height * 4, 0, -height)]
    )
    x_coords += [x for x in range(width * 2, width * 7, width)]
    y_coords += [height * 2] * 5

    # Letter L
    x_coords += [x for x in range(width * 11, width * 16, width)]
    y_coords += [height] * 5

    x_coords += [width * 11] * 4
    y_coords += [y for y in range(height * 2, height * 6, height)]

    # Letter X
    x_coords += [x for x in range(width * 18, width * 23, width)] * 2
    y_coords += [y for y in range(height, height * 6, height)]
    y_coords += [y for y in range(height * 5, 0, -height)]

    x_y_coords = list(zip(x_coords, y_coords))
    for x_y in x_y_coords:
        list_rectangles.append(Rectangle(width, height, x_y[0], x_y[1]))

    Base.draw(list_rectangles, list_squares)
