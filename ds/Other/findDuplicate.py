seen = set()
uniq = [1,2,3,4,5,5,6,7,8]
for x in a:
    if x not in seen:
        uniq.append(x)
        seen.add(x)