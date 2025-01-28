## Array and Hashing

## List
- For list and you need both index and value -> you have to enumerate inside the for loop

## Hashmap
- You can initialize by just {}
- my_dict.get() to get a value
- my_dict.get(key, 0) to return 0 if a key is not found
- my_dict.add() to add a value

## Default dictionary
- it automatically creates a default list if the key is empty

## Tuple
- It is immutable and just like list on indexing and slicing
    - List is [1,2,3]
    - tuple is (1,2,3)
- You can also have mutable inside immutable

```bash
# Tuple containing a list
my_tuple = ([1, 2, 3], 4)
my_tuple[0][0] = 10  # Modifies the list inside the tuple
print(my_tuple)  # Output: ([10, 2, 3], 4)
# However, the tuple structure (outer container) cannot be changed.
```

```bash
# Strings are immutable
my_string = "hello"
new_string = my_string.replace("h", "j")  # Creates a new string
print(my_string)  # Output: hello (original string remains unchanged)
print(new_string)  # Output: jello

# Tuples are immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise an error
```
