package hsson.sgshsmath.lecture1.operation;

import hsson.sgshsmath.lecture1.vector.Line;

public interface Transformation {

	public Line translate(Line line);
	
	public Line rotate(Line line);
	
	public Line scale(Line line);
	
	public Line transform(Line line);
	
}
