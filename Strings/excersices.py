from zipp.glob import separate

def calculate_the_characters_frequency(word):
    dictionary = {}

    for i in word:

        if i in dictionary.keys():
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] =  1


    return dictionary

def concat_the_first_and_last_two_chars(word):

    length = len(word)
    if length < 2 :
        return 'Empty string'

    return word[0:2] + word[-2:] # or # return word[0:2]  + word[length-2: length]

def find_the_first_repeated_char(word):

   dict = {}
   for i in word:
       if i in dict:
           return i
       dict[i] = 1

def count_occurrences(word,search):

     return word.count(search)

def delete_character(word, char):

    return word.replace(char,"")

def find_common_values(str1, str2):

   set1 = set(str1)
   set2 = set(str2)

   return ''.join((set1.intersection(set2)))

def separate_input_based_on_capital_letters(sentence):

    new = sentence
    for index, x in enumerate(sentence):

        if x.isupper():

            if index == 0:
                continue

            start_point = new[0:index]
            end_point = new[index:]
            new = start_point + " " + end_point

    return new


word = input("Input a word")
print("The frequency of word's chars is : ",calculate_the_characters_frequency(word) )
print("The result of merging the first two and last two chars is : ",concat_the_first_and_last_two_chars(word) )
print("The first repeated char of the word is : ",find_the_first_repeated_char(word) )

######################

word = input("Input a word")
search_value = input("Input a character")
print("The occurrences of the given character is : ",count_occurrences(word,search_value) )
print("The result of deleting the given character is : ",delete_character(word,search_value) )

######################

input1 = input("Input a word")
input2 = input("Input a word")
print("The common values are : ",find_common_values(input1,input2) )

#####################
input = input("Input a string which includes capital letters")
print("Result : ",separate_input_based_on_capital_letters(input) )