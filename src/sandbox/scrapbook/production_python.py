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
