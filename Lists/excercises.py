from array import array
from gc import collect


def get_the_maximum_value(list_items):
    max_value = list_items[0]
    for i in list_items:
        if i > max_value:
            max_value = i

    return max_value

def check_for_subsets(input_list1,input_list2):

    return all(map(input_list1.__contains__, input_list2))

def count_unique_sublists(input_list):
    input_list = list(input_list)
    dictionary = {}
    for item in input_list:
        key = tuple(item)
        if key in dictionary.keys():
            dictionary[key] = dictionary[key] + 1
        else:
            dictionary[tuple(item)] = 1

    return dictionary

def find_the_smallest_requested_element(input_list,number):

    input_list = input_list.sort()
    dictionary = {}
    ##unique values
    for item in input_list:
        if item not in dictionary.values():
            dictionary[len(dictionary)]=item

    #count unique values

    if number > len(dictionary):
        print("There is no element")
        return

    return dictionary[number]


# input_list = list([1,7,3,10,15,3])
# print("The maximum value is :", get_the_maximum_value(input_list))
############################################################################
# input1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# input2 = [[1, 3], [13, 15, 17]]
# print("The maximum value is :", check_for_subsets(input1,input2))

#Write a Python program to count the number of unique sublists within a given list.
# original_list = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# print("Number of unique lists of the said list:", count_unique_sublists(original_list))


#Write a Python function to find the kth smallest element in a list
original_list = [8,3,0,12,40,3,4,22]
number = input("Give a number")
print("The kth smallest element in a list is:", find_the_smallest_requested_element(original_list,int(number)))


#Write a Python program to find all the pairs in a list whose sum is equal to a given value.