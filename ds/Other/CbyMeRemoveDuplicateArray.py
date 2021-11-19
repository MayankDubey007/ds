list = [1,2,4,4,6,7,7,8,9,5]
result = []
for i in list:
    if i not in result:
        result.append(i)
print(result)