# 2. Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.

dictionary = {"Flowers": 10, "Trees": 20, "Chairs": 6, "Firepit": 1, "Grill": 2, "Lights": 14}
sorted_keys = sorted(dictionary)

# 3. Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to
#    buy at the store. Sort the dictionary's keys into alphabetical order, and save them as a list called grocery_keys_sorted.

groceries = {
    "apples": 5,
    "pasta": 3,
    "carrots": 12,
    "orange juice": 2,
    "bananas": 8,
    "popcorn": 1,
    "salsa": 3,
    "cereal": 4,
    "coffee": 5,
    "granola bars": 15,
    "onions": 7,
    "rice": 1,
    "peanut butter": 2,
    "spinach": 9,
}

grocery_keys_sorted = sorted(groceries)

# 4. Sort the following dictionary's keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values

dictionary = {"Flowers": 10, "Trees": 20, "Chairs": 6, "Firepit": 1, "Grill": 2, "Lights": 14}

sorted_values = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)

# Second Sort - Breaking Ties
# we use a set inside of the sort function. Sets sort from left to right most value to break ties

fruits = ["peach", "kiwi", "apple", "blueberry", "papaya", "mango", "pear", "pe", "qe"]

# here the body of the lambda returns a set
sorted_fruits = sorted(fruits, key=lambda value: (len(value), value), reverse=True)

print(sorted_fruits)
print()

# 3. Create a dictionary frequency_dict that stores the count of each number in the list.
print("3. Create a dictionary")

L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]

frequency_dict: dict[str, int] = {}
for letter in L:
    if letter in frequency_dict:
        frequency_dict[str(letter)] += 1
    else:
        frequency_dict[str(letter)] = 1

print(frequency_dict)
print()

# 4. Sort the numbers based on their frequency and store the top five keys in most_frequent_keys.
#    Review Sorting a Dictionary if you're not sure how to do this.
print("4. Sort the numbers")

L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]
frequent_keys: dict[str, int] = {}
for letter in L:
    if letter in frequent_keys:
        frequent_keys[str(letter)] += 1
    else:
        frequent_keys[str(letter)] = 1

most_frequent_keys = sorted(frequent_keys, key=lambda item: frequent_keys[item], reverse=True)[:5]

print(most_frequent_keys)
print()


# Write code to switch the order of the winners list so that it is now A to Z by last name.
# Assign this list to the variable z_winners.
print("Write code to switch the order")

winners = ["Alice Munro", "Alvin E. Roth", "Kazuo Ishiguro", "Malala Yousafzai", "Rainer Weiss", "Youyou Tu"]

l_winners = sorted(winners, key=lambda person: person.split()[-1], reverse=True)

print(l_winners)
print()
