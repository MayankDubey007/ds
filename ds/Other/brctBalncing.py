# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
print(["[","{","("])
print(["]","}",")"])
print("{,[,],{,(,),},}")
def check(myStr):
	stack = []
	print(stack)
	for i in myStr:
		if i in open_list:
			stack.append(i)
			print(F"STACK = {stack}")
			# print(f"open =  index->{open_list.index(i)}  and Ovalue->{open_list[open_list.index(i)]}")
		elif i in close_list:
			pos = close_list.index(i)
			print(f"pos,{pos} == close_list.index(i),{stack[len(stack)-1]}")
			print(f"{pos}{open_list[pos]} == {stack[len(stack)-1]},,stacklen- 1={(len(stack)-1)}")
			if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
				print(f"pop = {stack.pop()}")
				# stack.pop()
			else:
				return "Unbalanced"
	if len(stack) == 0:
		return "Balanced"
	else:
		return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string,"-", check(string))

string = "[{}{})(]"
print(string,"-", check(string))

string = "((()"
print(string,"-",check(string))
string = "(a+b)"
print(string,"-",check(string))
