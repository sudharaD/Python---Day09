starting_dictionary = {
    "a": 1,
    "b": 8,
}

# print(starting_dictionary[1])

starting_dictionary["c"] = 7

starting_dictionary[1] = 34


final_dictionary = starting_dictionary

print(final_dictionary)


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[1] += 1
    print(key)