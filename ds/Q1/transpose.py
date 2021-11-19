# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
print(f"ROW Length = len(X) = {len(X)}")
print(f"COLUMN Length = len(X[0]) = {len(X[0])}")
for r in range(len(X)):
   # iterate through columns
   for c in range(len(X[0])):
       print("________________________________")
       print("result[c][r] = X[r][c]")
       print(f"result[{c}][{r}] = X[{r}][{c}]")
       print(f"{result[c][r]} = {X[r][c]}")
       result[c][r] = X[r][c]
       print("----------------------------------")

for A in result:
   print(A)
