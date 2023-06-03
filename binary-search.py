#!/usr/bin/env python3

# ^ A shebang line defines where the interpreter is located. In this case, the python3 interpreter is located in /usr/bin/python3.Without the shebang line, the operating system does not know it's a python script. (Interesting!)

#Binary search is an algorithm; its input is a sorted list of elements looking for is in that list, binary search returns the position where it’s located

def binary_search(list, item):
    # Low and high to keep track of which part of the list you'll search in
    low = 0
    high = len(list) - 1

    while low <= high:  # Continue search as long as lower index is lower or equal to high index
        mid = low + high   # Calulate the middle index
        guess = list[mid]   # Get the item at mid index
        if guess == item:  # If the guess is equal to the target item, return the index
            return mid
        if guess > item:  # If the guess is greater than the target item, adjust the higher index
            high = mid - 1
        else:
            # If the guess is less than the target item, adjust the lower index
            low = mid + 1
    return None  # Return None if the target item is not found in the list.


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
