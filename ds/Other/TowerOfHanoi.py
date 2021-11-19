def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
n = 2
TowerOfHanoi(n, "source", "destination", "auxiliary")

# TowerOfHanoi(n  , source, destination, auxiliary): trick S D A 
# TowerOfHanoi(n-1, source, auxiliary, destination)        S A D
# TowerOfHanoi(n-1, auxiliary, destination, source)        A D S