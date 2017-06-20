package hsson.sgshsmath.lecture1.vector;

import java.util.Vector;

public class Point {

	private Vector<Double> poi = new Vector<Double>();
	
	public Vector<Double> getPoi(){
		return this.poi;
	}
	
	public int getVectorSize(){
		return this.poi.size();
	}
	
	public void setPoi(Vector<Double> poi){
		this.poi = poi;
	}

	public void setPoi(Vector<Double> poi, int idx){
		this.poi = poi;
	}

}
