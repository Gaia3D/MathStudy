package lecture1.hsson.sgshsmath.vector;

import java.util.Vector;

public class Line {

	public final int X = 0;
	public final int Y = 1;
	private Vector<Double> poi1 = new Vector<Double>();
	
	private Vector<Double> poi2 = new Vector<Double>();
	
	public Line(){
		this.poi1.addElement(0.0);
		this.poi1.addElement(0.0);
		this.poi2.addElement(0.0);
		this.poi2.addElement(0.0);
	}
	
	public Vector<Double> getPoi1(){
		return this.poi1;
	}
	
	public Double getPoi1(int idx) throws Exception{
		if(idx != this.X && idx != this.Y){
			throw new Exception("dememsion exception!!!");
		}
		return this.poi1.get(idx);
	}
	
	public Vector<Double> getPoi2(){
		return this.poi2;
	}
	
	public Double getPoi2(int idx) throws Exception{
		if(idx != this.X && idx != this.Y){
			throw new Exception("dememsion exception!!!");
		}
		return this.poi2.get(idx);
	}
	
	public int getVectorSize(){
		return this.poi1.size();
	}
	
	public void setPoi1(Vector<Double> poi1) throws Exception{
		if (poi1.size() != 2)
			throw new Exception("demension overflow!!!");
		this.poi1 = poi1;
	}

	public void setPoi1(Double scalar, int idx) throws Exception{
		if(idx != this.X && idx != this.Y){
			throw new Exception("dememsion exception!!!");
		}
		this.poi1.set(idx, scalar);
	}

	public void setPoi2(Vector<Double> poi2) throws Exception{
		if (poi2.size() != 2)
			throw new Exception("demension overflow!!!");
		this.poi2 = poi2;
	}
	

	public void setPoi2(Double scalar, int idx) throws Exception{
		if(idx != this.X && idx != this.Y){
			throw new Exception("dememsion exception!!!");
		}
		this.poi2.set(idx, scalar);
	}
	
	public String toString(){
		return this.poi1.toString() + " " + this.poi2.toString();
	}
}
