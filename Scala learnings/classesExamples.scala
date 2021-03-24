class Addition(val firstNumber:Int,val secondNumber:Int){
	var num_1:Int = firstNumber;
	var num_2:Int = secondNumber;

	def addition(param_1:Int,param_2:Int){
		var addedValue = param_1 + param_2
		println("Inside Addition method of class Addition : "+addedValue)
	}
}

class Calculator(override val firstNumber:Int,override val secondNumber:Int, val thirdNumber:Int) extends Addition(firstNumber,secondNumber){
	var num_3:Int = thirdNumber;

	def addition(param_1:Int,param_2:Int,param_3:Int){
		var addedValue = param_1 + param_2 + param_3
		println("Inside Addition method of class Calculator : "+addedValue)
	}
}

object classesExamples{
	def main(args: Array[String]){
		val calculator_obj = new Calculator(10,20,30)
		calculator_obj.addition(20,30,40);
	}
}