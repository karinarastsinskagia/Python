# Import the Counter class from the collections module
import collections
from collections import Counter
from collections import ChainMap
from collections import OrderedDict


def count_most_common_chars(str,number):
    return Counter(str).most_common(int(number))

def count_occurrences(sequence,num):

    sequence_dq = collections.deque(nums)
    return sequence_dq.count(num)

def merge_dictionaries(*dictionaries):
    # 1st way
    new = {}
    for arg in dictionaries:
        new.update(arg)

    #2nd way
    #return dict(ChainMap(dict1, dict2)))

    return new

def create_ordered_dict(original_dictionary):

    new = sorted(original_dictionary.items(),key=lambda x:x[1], reverse=True)
    new = dict(new)

    return OrderedDict(new.items())


# #Write a Python program to find the most common elements and their counts in a specified text.
original_string =  'lkseropewdssafsdfafkpwe'
top = input("Give a number for top common characters")
print("The top", top, "common characters in string : ",original_string," are : ", count_most_common_chars(original_string,top))

# #Write a  Python program to count the number of times a specific element appears in a deque object.
nums = (2, 9, 0, 8, 2, 4, 0, 9, 2, 4, 8, 2, 0, 4, 2, 3, 4, 0)
number = input("Which number occurrences do you want to learn?")
print("Number of ",number," in the sequence appears ",count_occurrences(nums,int(number)),"times")
#
# #Write a Python program to merge more than one dictionary into a single expression.
dict1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
dict2 = {'G': 'Green', 'W': 'White'}
print("The result of merging dictionaries : ", merge_dictionaries(dict1, dict2))

#Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
dictionary = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
print("Result : ", create_ordered_dict(dictionary))