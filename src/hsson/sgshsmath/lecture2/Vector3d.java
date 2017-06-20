package hsson.sgshsmath.lecture2;

public class Vector3d {
	
	private double x = 0;
	private double y = 0;
	private double z = 0;
	private double w = 0;
	
	public Vector3d(){
		this(0,0,0,0);
	}
	
	public Vector3d(double x, double y, double z, double w){
		this.x = x;
		this.y = y;
		this.z = z;
		this.w = w;
		
	}
	
	public double getVectorX(){
		return this.x;
	}
	
	public double getVectorY(){
		return this.y;
	}
	
	public double getVectorZ(){
		return this.z;
	}
	
	public double getVectorW(){
		return this.w;
	}
	
	public void setVectorX(double x){
		this.x = x;
	}
	
	public void setVectorY(double y){
		this.y = y;
	}
	
	public void setVectorZ(double z){
		this.z = z;
	}
	
	public void setVectorW(double w){
		this.w = w;
	}
	

	public String toString(){
		System.out.println("this vector's value = ("+this.x + ", " + this.y + ", " + this.z + ", " + this.w + ")");
		return "("+this.x + ", " + this.y + ", " + this.z + ", " + this.w + ")";
	}
	
	/**
	 * x축 기준으로 회전
	 * @param d : radian
	 * @throws Exception("rotation cannot transform this vector!!!") 
	 */
	public void rotateX(double d) throws Exception{
		
		this.toString();
		this.y = this.y * Math.cos(z) - this.z * Math.sin(z);
		this.z = this.y * Math.sin(z) + this.z * Math.cos(z);
		this.toString();
	}
	/**
	 * y축 기준으로 회전
	 * @param y : radian
	 * @throws Exception("rotation cannot transform this vector!!!") 
	 */
	public void rotateY(double y) throws Exception{
		
		this.toString();
		this.z = this.z * Math.cos(z) - this.x * Math.sin(z);
		this.x = this.z * Math.sin(z) + this.x * Math.cos(z);
		this.toString();
	}
	/**
	 * z축 기준으로 회전
	 * @param z : radian
	 * @throws Exception("rotation cannot transform this vector!!!") 
	 */
	public void rotateZ(double z) throws Exception{
		
		this.toString();
		this.x = this.x * Math.cos(z) - this.y * Math.sin(z);
		this.y = this.x * Math.sin(z) + this.y * Math.cos(z);
		this.toString();
	}

	/**
	 * 사원수를 이용한 회전ㅑㅔ 
	 * @param x : radian
	 * @param y : radian
	 * @param z : radian
	 * @throws Exception("rotation cannot transform this vector!!!") 
	 */
	public void rotate(double x, double y, double z) throws Exception{
		
		this.toString();
	}
}
