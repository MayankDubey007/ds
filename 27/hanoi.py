def hanoi(n,src,dst,aux):
    if n==1:
        print("move disk 1 from",src,"to",dst)
    else:
        hanoi(n-1,src, aux,dst)
        print("move disk",n,"from",src,"to",dst)
        hanoi(n-1,aux,dst,src)
n = 2
hanoi(n,"original","destination","auxilery")