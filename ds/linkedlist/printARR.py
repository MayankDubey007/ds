arr = [23,5,26,3,85,7346,3636,36,8,3,464,83]
# printway 01 Forward
print(arr)

# printway 02 Forward With Loop
for i in arr:
    print(i,end=", ")
print("\n")

# printway 03 Reverse
print(list(reversed(arr)))

# printway 04 Reverse with loop

for i in list(reversed(arr)):
    print(i,end=", ")
    break
print("\n")
# printway 05 Reverse with loop
for i in reversed(range(0,len(arr))):
    print(arr[i],end=", ")