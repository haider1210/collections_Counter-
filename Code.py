from collections import Counter                             ## Counter
It looks like you've provided examples of using the `Counter` class from the `collections` module in Python. `Counter` is a convenient tool for counting 
the occurrences of elements in an iterable or a mapping.

A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
 Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
   
Here's a brief explanation of each example:

1. `c = Counter()`: Creates a new, empty counter.

2. `c = Counter('gallahad')`: Creates a new counter from the characters in the iterable 'gallahad',
         counting the occurrences of each character.

3. `c = Counter({'red': 4, 'blue': 2})`: Creates a new counter from the mapping {'red': 4, 'blue': 2}, where keys are elements and values are their counts.

4. `c = Counter(cats=4, dogs=8)`: Creates a new counter from keyword arguments, where 'cats' and 'dogs' are elements, and 4 and 8 are their respective counts.

These examples demonstrate the flexibility of the `Counter` class in creating counters from various types of input data. You can then use the resulting counters
   to efficiently count occurrences of elements or perform other operations based on counting.

   Code :
   
from collections import Counter

# Example 1: Counting characters in a string
s = "abracadabra"
char_count = Counter(s)
print(char_count)
# Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Example 2: Counting words in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)
# Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Example 3: Combining Counters
counter1 = Counter({'a': 3, 'b': 2})
counter2 = Counter({'b': 1, 'c': 4})
combined_counter = counter1 + counter2
print(combined_counter)
# Output: Counter({'a': 3, 'b': 3, 'c': 4})

# Example 4: Accessing counts
print(char_count['a'])  # Output: 5

# Example 5: Most common elements
most_common = char_count.most_common(2)
print(most_common)
# Output: [('a', 5), ('b', 2)]



