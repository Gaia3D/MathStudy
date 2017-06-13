# -*- coding: utf-8 -*-

import math
from object.Point import Point


class LineString:

    RADIAN = "radian"
    DEGREE = "degree"

    _startX = 0.0
    _startY = 0.0
    _endX = 0.0
    _endY = 0.0

    def __init__(self,
                 startX,  # type: float
                 startY,  # type: float
                 endX,  # type: float
                 endY  # type: float
                 ):
        self._startX = startX
        self._startY = startY
        self._endX = endX
        self._endY = endY

    def getPoint(self):
        return self._startX, self._startY, self._endX, self._endY

    def getWKT(self):
        return "LINESTRING(%f %f, %f %f)" % (self._startX, self._startY, self._endX, self._endY)

    def translate(self, x, y):
        # type: (float, float) -> bool
        result = True

        if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
            self._startX += x
            self._startY += y
            self._endX += x
            self._endY += y

        else:
            print "숫자를 입력해야합니다 !!"
            result = False

        return result

    # rotating lineString by starting point
    def rotate(self, angle, unit=RADIAN):
        # type: (float, str) -> bool
        result = False

        try:

            if unit == self.DEGREE:
                angle = (angle * math.pi) / 180

            # move endPoint
            endPointX = self._endX - self._startX
            endPointy = self._endY - self._startY

            # get rotated endpoint
            rotatePointX = (endPointX * math.cos(angle)) - (endPointy * math.sin(angle))
            rotatePointY = (endPointX * math.sin(angle)) + (endPointy * math.cos(angle))

            self._endX = rotatePointX + self._startX
            self._endY = rotatePointY + self._startY

            result = True

        except Exception as e:
            print e

        return result

    def scale(self, num):
        # type: (float) -> bool
        result = False

        if not num == 0:
            self._endX = (self._endX - self._startX) * num + self._startX
            self._endY = (self._endY - self._startY) * num + self._startY

            result = True

        return result

    def transform(self, xMovement, yMovement):
        # type: (float, float, str) -> bool
        result = False

        try:
            tmp_x = self._endX - self._startX
            tmp_y = self._endY - self._startY

            if not xMovement == 0:
                self._endX = (tmp_x + tmp_y * xMovement) + self._startX

            if not yMovement == 0:
                self._endY = (tmp_y + tmp_x * xMovement) + self._startY

            result = True

        except Exception as e:
            print e

        return result

    def add(self, otherLine):
        # type: (LineString) -> bool
        result = True

        if otherLine.__class__ == LineString:
            otherStartX, otherStartY, otherEndX, otherEndY = otherLine.getPoint()

            xAmount = abs(otherStartX - otherEndX)
            yAmount = abs(otherStartY - otherEndY)

            self._endX += xAmount
            self._endY += yAmount

        else:
            print "파라미터 타입이 잘못되었습니다 !!"
            result = False

        return result

    def subtract(self, otherLine):
        # type: (LineString) -> bool
        result = True

        if otherLine.__class__ == LineString:
            otherStartX, otherStartY, otherEndX, otherEndY = otherLine.getPoint()

            xAmount = abs(otherStartX - otherEndX)
            yAmount = abs(otherStartY - otherEndY)

            self._endX -= xAmount
            self._endY -= yAmount

        else:
            print "파라미터 타입이 잘못되었습니다 !!"
            result = False

        return result

    def dotProduct(self, otherLine):
        # type: (LineString) -> float
        result = None

        if otherLine.__class__ == LineString:

            otherStartX, otherStartY, otherEndX, otherEndY = otherLine.getPoint()

            otherX = otherEndX - otherStartX
            otherY = otherEndY - otherStartY

            originX = self._endX - self._startX
            originY = self._endY - self._startY

            result = originX*otherX + originY*otherY

        else:
            print "파라미터 타입이 잘못되었습니다 !!"

        return result

    def crossProduct(self, otherLine):
        # type: (LineString) -> float
        result = None

        if otherLine.__class__ == LineString:

            otherStartX, otherStartY, otherEndX, otherEndY = otherLine.getPoint()

            otherX = otherEndX - otherStartX
            otherY = otherEndY - otherStartY

            originX = self._endX - self._startX
            originY = self._endY - self._startY

            result = originX * otherY - originY * otherX

        else:
            print "파라미터 타입이 잘못되었습니다 !!"

        return result

    def length(self):

        x = self._endX - self._startX
        y = self._endY - self._startY

        result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        return result  # type: float

    def normalize(self):
        result = True

        try:
            lineStringLength = self.length()

            x = self._endX - self._startX
            y = self._endY - self._startY

            self._endX = x / lineStringLength + self._startX
            self._endY = y / lineStringLength + self._startY

        except Exception as e:
            print e
            result = False

        return result

    def angleWith(self, otherLine):
        result = None

        if otherLine.__class__ == LineString:

            dotProductResult = self.dotProduct(otherLine)

            otherLength = otherLine.length()
            length = self.length()

            result = math.acos(dotProductResult / (length*otherLength))

        else:
            print ""

        return result

    def getNormalVector(self):
        normalVector = None

        try:
            lineStringLength = self.length()

            x = self._endX - self._startX
            y = self._endY - self._startY

            newEndX = x / lineStringLength
            newEndY = y / lineStringLength

            normalVector = LineString(0, 0, newEndX, newEndY)

        except Exception as e:
            print e

        return normalVector

    def distanceTo(self, pointObject):
        # type: (Point) -> float
        result = None

        try:
            if pointObject.__class__ == Point:
                pointX, pointY = pointObject.getPoint()

                dot = self.dotProduct(LineString(self._startX, self._startY, pointX, pointY))
                length = self.length()

                # 점의 위치 판단
                # r = 0   P = A
                # r = 1   P = B
                # r < 0   P is on the backward extension of AB
                # r > 1   P is on the forward extension of AB
                # 0 < r < 1   P is interior to AB
                r = dot / math.pow(length, 2)

                s = ((self._startY - pointY)*(self._endX - self._startX)
                     -(self._startX - pointX)*(self._endY - self._startY)) / math.pow(length, 2)

                result = abs(s) * length

        except Exception as e:
            print str(e)

        return result

    def intersectWith(self, otherLine):
        # type: (LineString) -> Point
        result = None

        if otherLine.__class__ == LineString:
            crossProduct = self.crossProduct(otherLine)

            if not crossProduct == 0: # 0 이면 평행함
                otherStartX, otherStartY, otherEndX, otherEndY = otherLine.getPoint()

                a = (self._startX * self._endY - self._startY * self._endX)
                b = (otherStartX * otherEndY - otherStartY * otherEndX)

                x = (a * (otherStartX - otherEndX) - b * (self._startX - self._endX)) / crossProduct
                y = (a * (otherStartY - otherEndY) - b * (self._startY - self._endY)) / crossProduct

                result = Point(x, y)

            else:
                print "두 선분은 평행합니다."

        return result