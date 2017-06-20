package hsson.sgshsmath.lecture1.operation.impl;

import hsson.sgshsmath.lecture1.operation.BasicOperation;
import hsson.sgshsmath.lecture1.vector.Line;

public class BasicOperationImpl implements BasicOperation{

	@Override
	public Line plus(Line line1, Line line2) throws Exception {
		// TODO Auto-generated method stub
		
		Line line = new Line();
		
		line.setPoi1(line1.getPoi1(line1.X) + line2.getPoi1(line1.X), line1.X);
		line.setPoi1(line1.getPoi1(line1.Y) + line2.getPoi1(line1.Y), line1.Y);
		line.setPoi2(line1.getPoi2(line1.X) + line2.getPoi2(line1.X), line1.X);
		line.setPoi2(line1.getPoi2(line1.Y) + line2.getPoi2(line1.Y), line1.Y);
		return line;
	}

	@Override
	public Line minus(Line line1, Line line2) throws Exception {
		// TODO Auto-generated method stub
		
		Line line = new Line();
		
		line.setPoi1(line1.getPoi1(line1.X) - line2.getPoi1(line1.X), line1.X);
		line.setPoi1(line1.getPoi1(line1.Y) - line2.getPoi1(line1.Y), line1.Y);
		line.setPoi2(line1.getPoi2(line1.X) - line2.getPoi2(line1.X), line1.X);
		line.setPoi2(line1.getPoi2(line1.Y) - line2.getPoi2(line1.Y), line1.Y);
		return line;
	}

	@Override
	public double dotProduct(Line line1, Line line2) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public Line crossProduct(Line line1, Line line2) {
		// TODO Auto-generated method stub
		return null;
	}

}
