array = [4,5,7,3,25,6,53,34,2,0]
print array

def sort1(arr):
    for i in range(len(arr)-1, 0, -1):
	    for j in range(0, i):
		    if arr[j] > arr[j+1]:
			    arr[j], arr[j+1] = arr[j+1], arr[j]

sort1(array)
print array