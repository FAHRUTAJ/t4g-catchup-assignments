# Task 1: Variables
first_name = "Fahrutaj"
last_name = "Nurudeen"
age = 25
fav_concept = "List Comprehension"
print(first_name, last_name, age, fav_concept)

# Task 2: Concatenation vs F-Strings
full_name = first_name + "," + last_name
print(full_name)
full_name= f"{first_name} {last_name}"
print(full_name)

# Task 3: String Methods
print(full_name.upper())
print(full_name.lower())
print(full_name.lower().count('a'))
print(full_name.find(" "))
print(full_name.replace(first_name, "Coder"))
print(len(full_name))
# Task 4: Sentence Introduction
sentence = f"Hi, I am {full_name}. I am {age} years old and my favourite concept so far is {fav_concept}."
print(sentence)

# Task 5: Indexing and Slicing
print(full_name[0])          # First char
print(full_name[-1])         # Last char
space_idx = full_name.find(" ")
print(full_name[0:space_idx]) # Slicing first name