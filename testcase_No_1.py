import Question_No_1 as codes
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
    fizzbuzzTestSuite = { 1:['1'], 2:['1','2'], 3:['1','2','FIZZ'], 5:['1','2','FIZZ','4','BUZZ'], 17:['1', '2', 'FIZZ', '4', 'BUZZ', 'FIZZ', '7', '8', 'FIZZ', 'BUZZ', '11', 'FIZZ', '13', '14', 'FIZZBUZZ', '16', '17'] }
    runTestSuite( codes.bappyFizz, fizzbuzzTestSuite )