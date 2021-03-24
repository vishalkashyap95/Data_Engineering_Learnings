object firstProgram{
	def main(args: Array[String]){

		// Variable declarations
		println("Execution Started!!");
		var myVarString = "Mutable string";
		val myValString = "Immutable string";
		println("This is Mutable String : "+myVarString);
		println("This is Immutable String : "+myValString);

		var empId:Int = 42442;
		val bankAccountNumber:Long = 836596348343L;
		println("Declared and assigned value to mutable empId variable : "+empId.toString);
		println("Declared and assigned value to immutable bankAccountNumber variable : "+bankAccountNumber.toString);

		var booleanVar:Boolean=true;
		println("Boolean variable: "+booleanVar);
	}
}