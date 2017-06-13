package lecture1.hsson;

import lecture1.hsson.sgshsmath.operation.*;
import lecture1.hsson.sgshsmath.operation.impl.*;
import lecture1.hsson.sgshsmath.vector.Line;

public class Solution {

	public static void main(String[] args) throws Exception{
		Line line1 = new Line();
		Line line2 = new Line();

		line1.setPoi1(10.0, line1.X);
		line1.setPoi1(10.0, line1.Y);
		line1.setPoi2(30.0, line1.X);
		line1.setPoi2(40.0, line1.Y);

		line2.setPoi1(20.0, line1.X);
		line2.setPoi1(20.0, line1.Y);
		line2.setPoi2(40.0, line1.X);
		line2.setPoi2(30.0, line1.Y);

		System.out.println("line1 = " + line1);
		System.out.println("line2 = " + line2);
		
		BasicOperation basicOperation = new BasicOperationImpl();
		System.out.println("line1 + line2 = " + basicOperation.plus(line1, line2));
		System.out.println("line1 - line2 = " + basicOperation.minus(line1, line2));
		
		
	}
	
}
