# -*- coding: utf-8 -*-


class Point:

    _x_point = 0.0
    _y_point = 0.0

    def __init__(self,
                 x_point,  # type: float
                 y_point  # type: float
                 ):
        self._x_point = x_point
        self._y_point = y_point

    def getPoint(self):
        return self._x_point, self._y_point

    def getWKT(self):
        return "POINT(%f %f)" % (self._x_point, self._y_point)
