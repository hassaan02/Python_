#   ========================== Variables and Data Types ================================

# Exercise 1: Create three variables: an integer, a float, and a string. Print their types

# num = 5
# float = 56.5
# str = "hassu"

# print(type(num))
# print(type(float))
# print(type(str))


# Exercise 2: Convert an integer to a float and vice versa. Print the results.

# int_value = 42
# float_value = 42.0

# convert_float = float(int_value)
# convert_int = int(float_value)

# print(convert_float)
# print(convert_int)


# ==========================  Strings ====================

# Exercise 1: Create a string and perform the following operations:
#     Find its length.
#     Convert it to uppercase.
#     Extract a substring.
#     Replace a word.

# str = "mynameishassaan"

# print(len(str))

# capt = str.upper()
# print(capt)

# sub_string = str[2:6]
# print(sub_string)

# replace = str.replace("hassaan", "ali")
# print(replace)


# Exercise 2: Concatenate two strings and print the result.

# str1 = "mynameishassaan"
# str2 = "andiamagoodboy"

# conct = str1 + str2
# print(conct)


# Exercise 3: Take user input as a string and check if it contains only digits.

# user_input = input("Write your name: ")

# if(user_input.isdigit()):
#     print("Yes it contaains digit")

# else:
#     print("it doesnt contain digit")

# ==================================== Lists and Tuples ===================================

# Exercise 1: Create a list of numbers. Perform the following:
#     Append a number to the list.
#     Remove a number from the list.
#     Sort the list in ascending order.

# list = [34,65,23,77,56,243]

# list.append(33)
# print(list)

# list.remove(243)
# print(list)

# list.sort()
# print(list)

# ======================== Conditional Expressions ===================

# Exercise 1: Write a Python program that asks the user for their age and prints whether they are eligible to vote (age >= 18).

# user_input = int(input("Write you age: "))

# if(user_input >= 18):
#     print("Yes, you are elegible to vote!")

# else:
#     print("No, you are not elegible for vote!")


# Exercise 2: Write a program that takes a number as input and checks if it is positive, negative, or zero.

# input = int(input("Write a number: "))

# if(input > 0):
#     print("Its a positive number!")

# elif(input < 0):
#     print("Its a negative number!")

# else:
#     print("Its a zer0")


# Using a conditional expression, print whether a given year is a leap year or not.

# year = int(input("Write a year: "))

# if(year % 4 == 0 and (year % 400 == 0 or year % 100 == 0)):
#     print("Its a leap Year!")

# else:
#     print("Its not a leap year")

# ===================  Dictionaries and Sets ===============================

# xercise 1: Create a dictionary with some key-value pairs. Perform the following:
#     Access a value using its key.
#     Add a new key-value pair.
#     Remove a key-value pair.

# dict = {
#     "Apple" : "Red",
#     "Avacado" : "Green",
#     "Mango" : "Yellow",
#     "Onion" : "Purple",
#     "Mooli" : "White"
# }

# dict["Mango"]
# dict["Carrot"] = "Orange"
# dict.pop("Mango")
# print(dict)


# Exercise 2: Create a set of unique numbers. Perform the following:
#     Add a new number to the set.
#     Try adding a duplicate number and observe the behavior.
#     Remove a number from the set.

# s = {1,2,3,4,5,6,7,8,9}

# s.add(10)
# s.add(5)
# s.remove(2)
# print(s)
