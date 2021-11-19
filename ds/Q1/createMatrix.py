r = int(input("Enter size Of Rows"))
c = int(input("Enter size Of columns"))
matricx = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matricx.append(a)
print("Entered Array's element are below")
for i in range(r):
    for j in range(c):
        print(matricx[i][j],end=" ")
    print()