#include "stdafx.h"
#include "Point3D.h"

#include <math.h>

Point3D::Point3D()
{
}

Point3D::Point3D(double x, double y, double z)
{
	this->x = x;
	this->y = y;
	this->z = z;
}

Point3D::~Point3D()
{
}

//////////////

void Point3D::set(double x, double y, double z)
{
	this->x = x;
	this->y = y;
	this->z = z;
}

double Point3D::magnitude()
{
	return sqrt(x*x + y*y + z*z);
}

bool Point3D::normalize()
{
	double mag = this->magnitude();
	if (mag >= tolerance || mag <= -tolerance)
	{
		x /= mag; y /= mag; z /= mag;
		return true;
	}
	else
	{
		x = 0.0; y = 0.0; z = 0.0;
		return false;
	}
}

double Point3D::angleWith(Point3D ref)
{
	Point3D thisVector = *(this);
	
	if (!ref.normalize() || thisVector.normalize())
		return 0.0;

	return acos(thisVector * ref);
}
