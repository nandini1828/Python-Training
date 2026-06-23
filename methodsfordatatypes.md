# Methods Useful for Data Types in Python

## String Methods

### upper()

Converts all characters in a string to uppercase.

### lower()

Converts all characters in a string to lowercase.

### capitalize()

Converts the first character of the string to uppercase and the rest to lowercase.

### title()

Converts the first character of every word to uppercase.

### strip()

Removes leading and trailing whitespace characters.

### lstrip()

Removes whitespace from the beginning of the string.

### rstrip()

Removes whitespace from the end of the string.

### replace(old, new)

Replaces all occurrences of a specified substring with another substring.

### split(separator)

Splits a string into a list using the specified separator.

### join(iterable)

Joins elements of an iterable into a single string using the specified separator.

### find(substring)

Returns the index of the first occurrence of a substring. Returns -1 if not found.

### index(substring)

Returns the index of the first occurrence of a substring. Raises an error if not found.

### count(value)

Returns the number of occurrences of a specified value.

### startswith(prefix)

Checks whether the string starts with the specified prefix.

### endswith(suffix)

Checks whether the string ends with the specified suffix.

### isalpha()

Returns True if all characters are alphabetic.

### isdigit()

Returns True if all characters are digits.

### isalnum()

Returns True if all characters are alphanumeric.

### swapcase()

Converts uppercase letters to lowercase and lowercase letters to uppercase.

### center(width)

Returns a centered string of the specified width.

---

# List Methods

### append(item)

Adds a single element to the end of the list.

### extend(iterable)

Adds multiple elements from an iterable to the end of the list.

### insert(index, item)

Inserts an element at a specified position.

### remove(item)

Removes the first occurrence of the specified element.

### pop(index)

Removes and returns the element at the specified index. Removes the last element if no index is provided.

### clear()

Removes all elements from the list.

### index(item)

Returns the index of the first occurrence of the specified element.

### count(item)

Returns the number of times an element appears in the list.

### sort()

Sorts the list in ascending order.

### reverse()

Reverses the order of elements in the list.

### copy()

Creates a shallow copy of the list.

---

# Tuple Methods

### count(item)

Returns the number of times an element appears in the tuple.

### index(item)

Returns the index of the first occurrence of an element.

---

# Dictionary Methods

### get(key)

Returns the value associated with a key. Returns None if the key does not exist.

### keys()

Returns a view containing all dictionary keys.

### values()

Returns a view containing all dictionary values.

### items()

Returns a view containing all key-value pairs.

### update(dictionary)

Updates the dictionary with key-value pairs from another dictionary.

### pop(key)

Removes the specified key and returns its value.

### popitem()

Removes and returns the last inserted key-value pair.

### clear()

Removes all key-value pairs from the dictionary.

### copy()

Creates a shallow copy of the dictionary.

### setdefault(key, default)

Returns the value of a key. If the key does not exist, inserts it with the specified default value.

---

# Set Methods

### add(item)

Adds a single element to the set.

### update(iterable)

Adds multiple elements from an iterable to the set.

### remove(item)

Removes the specified element. Raises an error if the element does not exist.

### discard(item)

Removes the specified element if present. Does not raise an error if not found.

### pop()

Removes and returns a random element from the set.

### clear()

Removes all elements from the set.

### copy()

Creates a shallow copy of the set.

### union(other_set)

Returns a new set containing elements from both sets.

### intersection(other_set)

Returns a new set containing common elements from both sets.

### difference(other_set)

Returns a new set containing elements present in the first set but not in the second.

### symmetric_difference(other_set)

Returns a new set containing elements that exist in either set but not in both.

### issubset(other_set)

Checks whether all elements of the set are present in another set.

### issuperset(other_set)

Checks whether the set contains all elements of another set.

### isdisjoint(other_set)

Checks whether two sets have no common elements.

---

# Common Built-in Functions

### len()

Returns the number of elements in an object.

### max()

Returns the largest element.

### min()

Returns the smallest element.

### sum()

Returns the sum of all elements.

### sorted()

Returns a sorted list from an iterable.

### type()

Returns the data type of an object.

### id()

Returns the unique memory address of an object.

### enumerate()

Returns an enumerate object containing index-value pairs.

### zip()

Combines multiple iterables element-wise.

---
