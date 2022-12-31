programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)

# Add item to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

print(programming_dictionary["Bug"])

print(["A", "B"][0])

# defining dictionary
empty_dictionary = {}

# Edit dictionary
programming_dictionary["Loop"] = "Loop is loop"

print(programming_dictionary)

# Clearing dictionary
programming_dictionary = {}

print(programming_dictionary)

letter_dictionary = {"A": "a", "B": "b", "C": "c"}

for i in letter_dictionary:
    print(i)
    print(letter_dictionary[i])
    