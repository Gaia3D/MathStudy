# -*- coding: utf-8 -*-

import math
import unittest
from object.LineString import LineString
from object.Point import Point

class LineStringTest(unittest.TestCase):

    lineString = None

    def setUp(self):
        self.lineString = LineString(1, 1, 3, 3)
        self.otherLineString = LineString(2, 2, 5, 4)

    def test_getWKT(self):
        print "origin : " + self.lineString.getWKT()

    def test_translate(self):
        result = self.lineString.translate(1, 3)
        self.assertTrue(result)
        print "translate : " + self.lineString.getWKT()

    def test_rotate(self):
        result = self.lineString.rotate(180, LineString.DEGREE)
        self.assertTrue(result)
        print "rotate : " + self.lineString.getWKT()

    def test_scale(self):
        result = self.lineString.scale(5)
        self.assertTrue(result)
        print "scale : " + self.lineString.getWKT()

    def test_transform(self):
        result = self.lineString.transform(2, 4)
        self.assertTrue(result)
        print "transform : " + self.lineString.getWKT()

    def test_add(self):
        result = self.lineString.add(self.otherLineString)
        self.assertTrue(result)
        print "add : " + self.lineString.getWKT()

    def test_subtract(self):
        result = self.lineString.subtract(self.otherLineString)
        self.assertTrue(result)
        print "subtract : " + self.lineString.getWKT()

    def test_dotProduct(self):
        result = self.lineString.dotProduct(self.otherLineString)
        self.assertIsNotNone(result)
        print "dotProduct : " + str(result)

    def test_crossProduct(self):
        result = self.lineString.crossProduct(self.otherLineString)
        self.assertIsNotNone(result)
        print "crossProduct : " + str(result)

    def test_length(self):
        result = self.lineString.length()
        print "length : " + str(result)

    def test_normalize(self):
        result = self.lineString.normalize()
        self.assertTrue(result)
        print "normalize / length : %s / %f " % (self.lineString.getWKT(), self.lineString.length())

    def test_angleWith(self):
        result = self.lineString.angleWith(self.otherLineString)
        self.assertIsNotNone(result)
        print "angle : %f (radian) / %f (degree) " % (result, (result * 180) / math.pi)

    def test_getNormalVector(self):
        normalVector = self.lineString.getNormalVector()
        self.assertIsNotNone(normalVector)
        print "normal vector / length : %s / %f" % (normalVector.getWKT(), normalVector.length())

    def test_distanceTo(self):
        point = Point(4,5)
        distance = self.lineString.distanceTo(point)
        self.assertIsNotNone(distance)
        print "distance : %f" % (distance)

    def test_intersectWith(self):
        result = self.lineString.intersectWith(self.otherLineString)
        self.assertIsNotNone(result)
        print "intersectWith : %s" % (result.getWKT())

if __name__ == '__main__':
    unittest.main()