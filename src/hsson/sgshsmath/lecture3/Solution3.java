package hsson.sgshsmath.lecture3;


public class Solution3 {

	public static void main(String[] args) throws Exception{
		
		Vector3d v1 = new Vector3d(1,2,0,0); 
		Vector3d v2 = new Vector3d(3,2,0,0); 
		Vector3d v3 = new Vector3d(3,4,0,0); 

		Vector3d v = new Vector3d(3,2,0,0); 

		//삼각형 만드는 v1,v2, v3를 이용해 벡터를 만들면...
		Vector3d V1 = new Vector3d(v2.getVectorX()-v1.getVectorX(), v2.getVectorY()-v1.getVectorY(), 0, 0);
		Vector3d V2 = new Vector3d(v3.getVectorX()-v1.getVectorX(), v3.getVectorY()-v1.getVectorY(), 0, 0);
		
		
		// a, b값 구해서 정리하면....
		double a = (V2.getVectorX()*v.getVectorY() - V2.getVectorY()*v.getVectorX())/ (V1.getVectorY()*V2.getVectorX() - V1.getVectorX() * V2.getVectorY()) ;

		double b = (V1.getVectorY()*v.getVectorX() - V1.getVectorX()*v.getVectorY())/ (V1.getVectorY()*V2.getVectorX() - V1.getVectorX() * V2.getVectorY()) ;

		System.out.println(a + ", " + b);
		if(a >= 0 && a <= 1 && b >= 0 && b <= 1 && a+b <= 1){
			System.out.println("벡터 " + v + "는 ....");
			System.out.println("삼각형 내부의 점입니다!!!");
		} else {
			System.out.println("벡터 " + v + "는 ....");
			System.out.println("삼각형 내부의 점이 아닙니다!!!");
		}
	}
	
}
