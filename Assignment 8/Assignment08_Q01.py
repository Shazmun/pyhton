#Assignment08_Q01

# Create dictionary
d = {'a': 15, 'c': 35, 'b': 10}

# all keys and all values
print("Keys:", ' '.join(d.keys()))
print("Values:", ' '.join(str(val) for val in d.values()))

# key-value pairs in tabular format
print("Key-Value pairs")
for key, value in d.items():
    print(key, value)

#key-value pairs in tabular format ordered by key
print("Key-Value pairs- sorted by key")
for key in sorted(d.keys()):
    print(key, d[key])

# key-value pairs in tabular format ordered by value
print("Key-Value pairs- sorted by value")
for key, value in sorted(d.items(), key=lambda item: item[1]):
    print(key, value)



