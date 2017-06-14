#include "stdafx.h"
#include "Line.h"

#include <math.h>

Line::Line()
{
}

Line::Line(Point3D& start, Point3D& end)
{
	startPoint = start;
	endPoint = end;
}

Line::~Line()
{
}

void Line::set(Point3D& start, Point3D& end)
{
	startPoint = start;
	endPoint = end;
}

double Line::length()
{
	Point3D diff = startPoint - endPoint;

	return diff.magnitude();
}

double Line::distanceTo(Point3D& target)
{
	Point3D v1 = startPoint - target;
	Point3D v2 = endPoint - target;

	Point3D v2to1 = v1 - v2;

	double numerator = v2to1.x * v2.x + v2to1.y * v2.y + v2to1.z + v2.z;
	double denominator = v2to1.magnitude() * v2to1.magnitude();
	double param = -numerator / denominator;

	if (param <= 0.0)
	{
		return v2.magnitude();
	}
	else if (param >= 1.0)
	{
		return v1.magnitude();
	}
	else
	{
		return sqrt(param*numerator + v2.magnitude()*v2.magnitude());
	}
}
