# -*- coding: utf-8 -*-

from figure.point import Point
from figure.triangle import Triangle

if __name__ == '__main__':
    point = Point(1, 3)

    triangle = Triangle(0, 4, 4, 0, 5, 5)

    print triangle.checkPointInThis(point)