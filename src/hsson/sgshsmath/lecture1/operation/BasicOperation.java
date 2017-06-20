package hsson.sgshsmath.lecture1.operation;

import hsson.sgshsmath.lecture1.vector.Line;

public interface BasicOperation {

	
	public Line plus(Line line1, Line line2) throws Exception;
	
	public Line minus(Line line1, Line line2) throws Exception;
	
	public double dotProduct(Line line1, Line line2);
	
	public Line crossProduct(Line line1, Line line2);
}
