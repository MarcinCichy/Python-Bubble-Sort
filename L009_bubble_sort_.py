def bubble_sort(datas):
	
	choice = input("Sortowanie malejące [M], czy rosnące [R]: ")
	for i in range(len(datas)):
		temp = None
		for j in range(1, len(datas)):
			if choice.lower() == "r":
				if datas[j-1] <= datas[j]:
					continue
			elif choice.lower() == "m":
				if datas[j-1] >= datas[j]:
					continue
			temp = datas[j-1]
			datas[j-1] = datas[j]
			datas[j] = temp
			print(i, '.', j, ' = ', datas)
	print("*"*40)
	print(f"Lista posortowana: {datas}")


print("*"*40)
listy = [[5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [], [1, 5, 7, 10, 11], [23, 5, 7, 46, 78, 98, 1, 4, 7989, 3, 1]]
for i in range(5):
	lista = listy[i]
	print(f"Lista wejściowa:  {lista} \n")
	bubble_sort(lista)
	print("\n")
	print("*" * 40)

# l1 = [5, 4, 3, 2, 1]
# l2 = [1, 1, 1, 1, 1]
# l3 = []
# l4 = [1, 5, 7, 10, 11]
# l5 = [23, 5, 7, 46, 78, 98, 1, 4, 7989, 3, 1]
