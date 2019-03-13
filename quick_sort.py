from random import randrange
grades = [95, 88, 91, 97, 100, 99, 89, 95, 93, 85]

def quick_sort(lst, start, end):
	# base case
	if start >= end:
		return lst
	# randomly selects a pivot index between this range
	pivot_index = randrange(start, end)	
	pivot_element = lst[pivot_index]
	# swap elements in list so your pivot element is at the end now
	lst[end], lst[pivot_index] = lst[pivot_index], lst[end]

	less_than_pointer = start

	for index in range(start, end):
		if lst[index] < pivot_element:
			lst[index], lst[less_than_pointer] = lst[less_than_pointer], lst[index]
			less_than_pointer += 1

	lst[end], lst[less_than_pointer] = lst[less_than_pointer], lst[end]	
	#sort left sublist	
	quick_sort(lst, start, less_than_pointer - 1)
	#sort right sublist	
  	quick_sort(lst, less_than_pointer + 1, end)

  	start+=1
  	return quick_sort(lst, start, end)

print("unsorted list: ")
print(grades)
sorted_list = quick_sort(grades, 0, len(grades)-1)
print("sorted list: ")
print(sorted_list)	