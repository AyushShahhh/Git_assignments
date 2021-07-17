import Question_No_2 as codes
def runTest( fun, input, output ):
	actualOutput = fun( input )
	return actualOutput, actualOutput == output
def runTestSuite( fun, testSuite ):
	for input, output in testSuite.items():
		actualOutput, status = runTest( fun, input, output )
		print("input: ", input )
		print("Exp. output: ", output)
		print("Act. output: ", actualOutput)
		print("test Status: ", status)
if __name__ == "__main__":
	print("FIBONACCI\n")
	fibonacciTestSuite = { 1:[1], 2:[1,1], 3:[1,1,2], 5:[1,1,2,3,5], 10:[1,1,2,3,5,8,13,21,34,55] }
	runTestSuite( codes.fibo, fibonacciTestSuite )