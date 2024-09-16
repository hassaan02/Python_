# 1. Write a program to find the greatest of four numbers entered by the user. 

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))

# greatest = num1

# if(num2 > greatest):
#     greatest = num2

# elif(num3 > greatest):
#     greatest = num3    

# elif(num4 > greatest):
#     greatest = num4

# print("The greatest number is: ", greatest)

# ===============================================================================================================

# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

# max_marks = 100

# sub1 = float(input("Enter the Marks of Subject 1: "))
# sub2 = float(input("Enter the Marks of Subject 2: "))
# sub3 = float(input("Enter the Marks of Subject 3: "))

# total_marks = sub1 + sub2 + sub3
# percentage = (total_marks / (3 * max_marks)) * 100

# if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
#     if(percentage >= 40):
#         print("you are Passed!")
#     else:
#         print("You are Faied!")

# else:
#     print("you are failed because of getting less marks in subject")             

# print(percentage,"%")     


# ===============================================================================================================

# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

# spam_keyw1 = "make a lot of money"   
# spam_keyw2 = "buy now"   
# spam_keyw3 = "subscribe this"   
# spam_keyw4 = "click this"

# user_input = input("Ente the comment: ")

# if spam_keyw1 in user_input or \
#    spam_keyw2 in user_input or \
#    spam_keyw3 in user_input or \
#    spam_keyw4 in user_input:
#     print("This comment contain SPAM")

# else:
#     print("This comment doesnt contain SPAM")  

# ===============================================================================================================

# Write a program to find whether a given username contains less than 10 
# characters or not. 

# username = input("Enter the username: ")

# if len(username) < 10:
#     print("Username is Less than 10 character")

# else:
#     print("Username is Greater than 10 characters")

# ===============================================================================================================

# 5. Write a program which finds out whether a given name is present in a list or not. 

# list = ["ali", "ahmed", "hassaan", "umar", "john"]

# user_input = input("Enter the name: ")


# if(user_input in list):
#     print("available")

# else:
#     print("not available")

# ====================================================================================================

# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 
 

# user_input = int(input("Enter the marks of student: "))

# if(90 <= user_input <= 100):
#     grade = "Ex"

# elif(80 <= user_input < 90 ):
#     grade = "A"

# elif(70 <= user_input < 80 ):
#     grade = "B"

# elif(60 <= user_input < 70 ):
#     grade = "C"

# elif(50 <= user_input < 60 ):
#     grade = "D"

# else:
#     grade = "F"

# print(f"The student's grade is: {grade}")

# ====================================================================================================


