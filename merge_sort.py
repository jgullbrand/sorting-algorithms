grades = [95, 88, 91, 97, 100, 99, 89, 95, 93, 85]

def merge_sort(lst):
	# this is the base case
	if len(lst) <= 1:
		return lst	
	middle_index = len(lst) // 2	
	left_split = lst[:middle_index]
	right_split = lst[middle_index:]

	# recursively calling on left split
	left_sort = merge_sort(left_split)
	# recursively calling on right split
	right_sort = merge_sort(right_split)

	# calling merge function to return the full sorted list.
	return merge(left_sort, right_sort)

#This is a helper function to merge the data together
def merge(left_list, right_list):
	results = []
	# this while loop continues to iterate while both these lists have elements in them
	while left_list and right_list:
		# checking if the left most value is smaller on the left or right list.
		if left_list[0] < right_list[0]:
			results.append(left_list[0])
			left_list.pop(0)
		else:
			results.append(right_list[0])
			right_list.pop(0)	
	# Checking if there are remaining items on either the left or right list
	if left_list:
		# if items on the left list, append to the result list
		results += left_list
	elif right_list:
		# if items on the right list, append to the result list
		results += right_list			

	return results	

print("unsorted list: ")
print(grades)
sorted_list = merge_sort(grades)
print("sorted list: ")
print(sorted_list)
