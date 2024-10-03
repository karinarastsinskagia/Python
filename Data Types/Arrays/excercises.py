# import numpy as np
from array import *


def add_new_element_in_array(initial_array, sequence_num, insert_num):
    for key, value in enumerate(initial_array):

        if value == int(sequence_num):
            initial_array.insert(key, int(insert_num))
            return initial_array

    return initial_array


def find_the_missing_item(original_array):
    completed_items = [10, 11, 12, 13, 15, 14, 16, 17, 18, 19, 20]
    # return np.setdiff1d(correct_array, original_array)

    result = [value for value in completed_items if value not in original_array]

    return result


# Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.
original_array = array("i", [1, 3, 5, 7, 9])
print("Current memory address and the length in elements of the buffer: " + str(original_array.buffer_info()))
print("The size of the memory buffer in bytes: " + str(original_array.buffer_info()[1] * original_array.itemsize))

# Write a Python program to append items from inerrable to the end of the array.
original_array = array('i', [1, 3, 5, 7, 9])
print("Extended array : ", original_array.__add__(original_array))
original_array.extend(original_array)
print("Extended array : ", original_array)

# Write a Python program to insert a newly created item before the second element in an existing array.
initial_array = array('i', [1, 3, 5, 7, 9])
insert_num = input("Give new number: ")
sequence_num = input("Put the new number before : ")
print("New Array is : ", add_new_element_in_array(initial_array, sequence_num, insert_num))

# Write a Python program to check whether it follows the sequence given in the patterns array.

# Write a  Python program to find the missing number in a given array of numbers between 10 and 20.
original_array = array("i", [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
print("Missing number in the array (10-20): is : ", find_the_missing_item(original_array))
