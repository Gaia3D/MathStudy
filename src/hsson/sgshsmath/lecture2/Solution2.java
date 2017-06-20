package hsson.sgshsmath.lecture2;


public class Solution2 {

	public static void main(String[] args) throws Exception{
		
		Vector3d vector3d = new Vector3d(1,2,3,0); 

		System.out.println("x축으로 45도 움직이면...");
		vector3d.rotateX(Math.PI/4);

		System.out.println("거기서 y축으로 45도 움직이면...");
		vector3d.rotateY(Math.PI/4);

		System.out.println("거기서 z축으로 45도 움직이면...");
		vector3d.rotateZ(Math.PI/4);

		
	}
	
}
