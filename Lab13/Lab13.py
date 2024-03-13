#Lab13

def intersect(dict_1, dict_2):
    result = {}
    for key, value in dict_1.items():
        if key in dict_2 and value == dict_2[key]:
            result[key] = value
    return result

def union(dict_1, dict_2):
    result = dict_1.copy()
    for key, value in dict_2.items():
        if key not in result:
            result[key] = value
    return result

def main():
    dict_1 = {}
    dict_2 = {}
    
    print("Enter 5 names with grades:")
    for i in range(5):
        name, score = input().split()
        dict_1[name] = score
    print()

    print("Enter another 5 names with grades:")
    for i in range(5):
        name, score = input().split()
        dict_2[name] = score
    print()

    print("Name          Age")
    for key, value in dict_1.items():
        print(f"{key:<15}{value:<15}")

    print("\nName          Age")
    for key, value in dict_2.items():
        print(f"{key:<15}{value:<15}")

    intersection_result = intersect(dict_1, dict_2)
    union_result = union(dict_1, dict_2)

    print(f"\nIntersection of dict1 and dict2 = {intersection_result}")
    print(f"Union of dict1 and dict2 = {union_result}")

if __name__ == "__main__":
    main()
