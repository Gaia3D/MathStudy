#pragma once
class Point3D
{
public:
	Point3D();
	Point3D(double x, double y, double z);
	virtual ~Point3D();

	double x, y, z;

public:
	void set(double x, double y, double z);
	
	double magnitude();
	
	bool normalize();

	double angleWith(Point3D ref);

	// operator overriding
	void operator = (const Point3D &q) { x = q.x; y = q.y; z = q.z; }

	Point3D operator - (const Point3D &q) const
	{
		Point3D t(x - q.x, y - q.y, z - q.z);
		return t;
	}

	Point3D operator + (const Point3D &q) const
	{
		Point3D t(x + q.x, y + q.y, z + q.z);
		return t;
	}

	Point3D operator ^ (const Point3D &v) const
	{
		Point3D t(y*v.z - v.y*z, v.x*z - x*v.z, x*v.y - v.x*y);
		return t;
	}

	double operator * (const Point3D &v) const
	{
		return (x*v.x + y*v.y + z*v.z);
	}

	void operator * (double valor)
	{
		x *= valor; y *= valor; z *= valor;
	}

	void operator / (double valor)
	{
		x /= valor; y /= valor; z /= valor;
	}

};

