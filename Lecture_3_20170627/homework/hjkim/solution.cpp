
// 삼각형의 세 꼭지점 : (x1, y1), (x2, y2), (x3, y3)
// 테스트 대상 점   : (x, y)
// 참고 : 위에서 봤을 때 꼭지점의 순서가 반시계 방향
// 대상 점이 삼각형의 변(edge) 위에 정확히 위치할 경우 outside로 판단했다.

// solution 1.
bool isPointInsideTriangle(double x1, y1,
							double x2, y2,
							double x3, y3,
							double x, y)
{
	// v1 = (x2, y2) - (x1, y1)
	// v2 = (x3, y3) - (x1, y1)
	// v  = (x, y) - (x1, y1)
	
	// v  = a v1 + b v2로 나타낼 수 있으므로 
	// a, b를 찾은 다음에
	// a <= 0 || a >= 1 || b <= 0 || b >= 1 || a+b >= 1 
	// 이 조건을 만족하면 대상 점은 삼각형 밖에 있다
	
	double denominator = (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1);
	double a = x * (y3 - y1) - y * (x3 - x1);
	double b = -x * (y2 - y1) + y * (x2 - x1);
	
	if(a <= 0.0 || a >= 1.0 || b <= 0.0 || b >= 1.0 || a+b >= 1.0)
		return false;
		
	return true;
}

// solution 2.
bool isPointInsideTriangle(double x1, y1,
							double x2, y2,
							double x3, y3,
							double x, y)
{
	// 삼각형의 각 변에 수직인 벡터 3개 각각에 
	// 삼각형과 대상 점의 그림자를 드리운 후(프로젝션 후)
	// 그림자가 겹치지 않을 경우 대상 점은 삼각형 밖에 있다.
	
	double MaxTriangleProjectionAlongEdge1 = x1*y2 - x2*y1;
	double MinTriangleProjectionAlongEdge1 = x3*(y2 - y1) - y3*(x2 - x1);
	double PointProjectionAlongEdge1 = x*(y2 - y1) - y*(x2 - x1);
	
	double MaxTriangleProjectionAlongEdge2 = x2*y3 - x3*y2;
	double MinTriangleProjectionAlongEdge2 = x1*(y3 - y2) - y1*(x3 - x2);
	double PointProjectionAlongEdge2 = x*(y3 - y2) - y*(x3 - x2);
	
	double MaxTriangleProjectionAlongEdge3 = x3*y1 - x1*y3;
	double MinTriangleProjectionAlongEdge3 = x2*(y1 - y3) - y2*(x1 - x3);
	double PointProjectionAlongEdge3 = x*(y1 - y3) - y*(x1 - x3);
	
	if( (PointProjectionAlongEdge1 <= MinTriangleProjectionAlongEdge1 ||
	     PointProjectionAlongEdge1 >= MaxTriangleProjectionAlongEdge1) ||
		 (PointProjectionAlongEdge2 <= MinTriangleProjectionAlongEdge2 ||
	     PointProjectionAlongEdge2 >= MaxTriangleProjectionAlongEdge2) ||
		 (PointProjectionAlongEdge3 <= MinTriangleProjectionAlongEdge3 ||
	     PointProjectionAlongEdge3 >= MaxTriangleProjectionAlongEdge3) )
		 return false;
	
	return true;
}

// solution 3.
bool isPointInsideTriangle(double x1, y1,
							double x2, y2,
							double x3, y3,
							double x, y)
{
	// 삼각형의 각 변의 시작점에서 끝점으로 이동할 때 
	// 해당 변을 기준으로 오른쪽을 바깥이라고 정의하고
	// 바깥쪽을 향하는 법선벡터로 삼각형의 세 변의 직선의 방정식을 구한후
	// 대상 점을 각 직선의 방정식에 대입하여
	// 3개의 직선 모두에 대해 안쪽에 있음을 테스트
	
	double pointOnLineEquation1 = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1);
	double pointOnLineEquation2 = (x - x2) * (y3 - y2) - (y - y2) * (x3 - x2);
	double pointOnLineEquation3 = (x - x3) * (y1 - y3) - (y - y3) * (x1 - x3);
	
	if( pointOnLineEquation1 >= 0.0 ||
		pointOnLineEquation2 >= 0.0 ||
		pointOnLineEquation3 >= 0.0 )
		return false;
		
	// 아래와 같이 테스트 해도 된다.
	// 왜 그럴까? 생각해봅시다.
	//if( pointOnLineEquation1 * pointOnLineEquation2 <= 0.0 ||
	//	pointOnLineEquation1 * pointOnLineEquation3 <= 0.0 )
	//	return false;
		
	return true;
}
