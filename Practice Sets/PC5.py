# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

# words_mean = {
#     "Serendipity" : "The occurrence of events by chance in a happy or beneficial way.",
#     "Euphoria" : "A feeling or state of intense excitement and happiness.",
#     "Ephemeral" : "Lasting for a very short time.",
#     "Nostalgia" : "A sentimental longing or affection for the past.",
#     "Solitude" : "The state or situation of being alone, often by choice."
# }

# word = input("Enter the word you want meaning of :")
# print("Meaning : ",words_mean[word])



# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

# s = set()

# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))
# user_input = input("Entered the number : ")
# s.add(int(user_input))

# print(s)



# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 

# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)


# 5. s = {} 
# What is the type of 's'?

# s = {}
# print(type(s))



# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

# d = {}

# name = input("enter friends name : ")
# lang = input("Enter favourite language : ")
# d.update({name : lang})

# name = input("enter friends name : ")
# lang = input("Enter favourite language : ")
# d.update({name : lang})

# name = input("enter friends name : ")
# lang = input("Enter favourite language : ")
# d.update({name : lang})

# name = input("enter friends name : ")
# lang = input("Enter favourite language : ")
# d.update({name : lang})

# print(d)


# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}

#   not possible No, you cannot have a list inside a set in Python because sets can only contain immutable (unchangeable) data types. Lists are mutable, meaning their elements can be changed, so they cannot be added to a set.