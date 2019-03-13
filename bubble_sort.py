grades = [95, 88, 91, 97, 100, 99, 89, 95, 93, 85]

def bubble_sort(lst):
	# outer loop - going through each element
	for element in lst:
		# Inner loop - going through to compare each element with every other list element
		for index in range(len(lst) - 1):
			# checking if the current list element is greater than the value to the right
			if lst[index] > lst[index+1]:
				# if the condition is true, perform a swap to move the greater value to the right
				lst[index], lst[index+1] = lst[index+1], lst[index]

print("unsorted list: ")
print(grades)

bubble_sort(grades)

print("sorted list: ")
print(grades)
