package lecture1.hsson.sgshsmath.operation;

import lecture1.hsson.sgshsmath.vector.Line;

public interface Transformation {

	public Line translate(Line line);
	
	public Line rotate(Line line);
	
	public Line scale(Line line);
	
	public Line transform(Line line);
	
}
