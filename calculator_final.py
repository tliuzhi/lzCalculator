function=input("do you want to use the calculator? input y for yes or n for no: ")
answer=str(function)
checkanswer=answer.find("y")
def calculator(first,second,operator):
	print("Value 1:",first)
	print("Value 2",second)
	print("Operator:",operator)
	if operator == "+":
		results = first + second
		print("results calculated:",results)
	if operator == "-":
		results = first - second
		print("results calculated:",results)
	if operator == "*":
		results = first * second
		print("results calculated:",results)
	if operator == "/":
		results = first / second
		print("results calculated:",results)

def isDigit(x):
	try:
		float(x)
		return True
	except ValueError:
		return False


while checkanswer != -1:
	one=input("Please key in first value:")
	two=input("Please key in second value:")
	operator=input("Please input an operator e.g. * / + -:")
	#second=float(two)
	#first=float(one)
	checkoperator=operator.find("/")
	if one == "" or two == "" or operator == "":
		print("value or operator cannot be empty!")
	elif isDigit(one) == False or isDigit(two) == False:
		print("please enter number only for the values!")
		#print(one.isdigit())
		#print(two.isdigit())        
	elif float(two) == 0 & checkoperator != -1:	 
		print("value cannot be divisible by 0") 
	elif operator != "+" and operator != "-" and operator != "/" and operator != "*":
		print("operator is not valid!")	   
	else:
		print(float(one))
		print(float(two))
		print(operator)
		calculator(float(one),float(two),operator)
	continue