package lecture1.hsson.sgshsmath.operation;

import lecture1.hsson.sgshsmath.vector.Line;

public interface BasicOperation {

	
	public Line plus(Line line1, Line line2) throws Exception;
	
	public Line minus(Line line1, Line line2) throws Exception;
	
	public double dotProduct(Line line1, Line line2);
	
	public Line crossProduct(Line line1, Line line2);
}
