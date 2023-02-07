list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = [1,3,5,7,9, 43]

for i in range(len(list2)-1):
	list1.remove(list2[i])

print(list1)