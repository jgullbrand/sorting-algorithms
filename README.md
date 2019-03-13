## Sorting Algorithms 
I explored three different sorting algorithms below: Bubble Sort, Merge Sort, Quick Sort. I've relied on the support of the python community and online resources to grasp a better understanding for these three sorting algorithms.

I attemped to explore these sorts through 1) a brief comparison outlined in the table below, 2) python code representation for each

I created a list of grades that could be used to test the different sorts.
[95, 88, 91, 97, 100, 99, 89, 95, 93, 85]

**1) A brief comparison of the three sorting algorithms:**

![updatedcomparison](https://user-images.githubusercontent.com/40340806/54310698-5aff9680-45a9-11e9-8cc4-7577ad33bc1a.png)

**2) Python code representation:**

**Bubble Sort**
```python
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
```


**Merge Sort**
```python
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
```

**Quick Sort**
```python
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
```
