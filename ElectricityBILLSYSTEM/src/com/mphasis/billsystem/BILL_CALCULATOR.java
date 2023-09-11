package com.mphasis.billsystem;

public class BILL_CALCULATOR {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int units = 280;
		double billtopay = 0;
		if(units < 100)
		{
			billtopay = units * 1.20;
		}
		else if(units < 300)
		{
			billtopay = 100 * 1.20 + (units - 100) *2;
		}
		
		System.out.println("The electricity bill for "+units+ "is :" +billtopay);

	}

}
