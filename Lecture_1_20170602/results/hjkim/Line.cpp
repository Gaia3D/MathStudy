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
}
