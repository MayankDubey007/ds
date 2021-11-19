# def getMissingNo(A):
#     n = len(A)
#     print(f"len = {n}")
#     total = (n + 1)*(n + 2)//2
#     sum_of_A = sum(A)
#     print(f"sum_of_A = {sum_of_A} ")
#     print(f"total = {total} ")
#     return total - sum_of_A


# # Driver program to test the above function
# A = [1,2,4, 5, 6, 7]
# miss = getMissingNo(A)
# print(miss)
# Python3 program to find
# the missing Number
# getMissingNo takes list as argument
def getMissingNo(a, n):
	n_elements_sum=n*(n+1)//2
	# return n_elements_sum-sum(a)
	# return n_elements_sum
 	return sum(a)


# Driver program to test above function
if __name__=='__main__':

	a = [1, 2, 4, 5, 6]
	n = len(a)+1
    # print(sum(a))
	miss = getMissingNo(a, n)
	print(miss)
