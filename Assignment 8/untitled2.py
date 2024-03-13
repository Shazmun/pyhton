#Assignment08_Q01

# Create dictionary
my_dict = {'a': 15, 'c': 35, 'b': 10}

# all keys and all values
print("Keys:", ' '.join(my_dict.keys()))
print("Values:", ' '.join(str(val) for val in my_dict.values()))

# key-value pairs in tabular format
print("Key-Value pairs")
for key, value in my_dict.items():
    print(key, value)

#key-value pairs in tabular format ordered by key
print("Key-Value pairs- sorted by key")
for key in sorted(my_dict.keys()):
    print(key, my_dict[key])

# key-value pairs in tabular format ordered by value
print("Key-Value pairs- sorted by value")
for key, value in sorted(my_dict.items(), key=lambda item: item[1]):
    print(key, value)
