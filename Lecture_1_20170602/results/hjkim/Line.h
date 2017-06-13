#pragma once

#include "Point3D.h"

class Line
{
public:
	Line();
	Line(Point3D& start, Point3D& end);
	virtual ~Line();

protected:
	Point3D startPoint;
	Point3D endPoint;

public:
	void set(Point3D& start, Point3D& end);

	double length();

	double distanceTo(Point3D& target);
};

