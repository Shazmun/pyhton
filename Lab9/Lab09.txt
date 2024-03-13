#Lab09

def evenNumbers(number_list):
    even = []
    for e in number_list:
        if e % 2 == 0:
            even.append(e)
    return even

def sumOdd(number_list):
    odd_sum = 0
    for e in number_list:
        if e % 2 != 0:
            odd_sum += e
    return odd_sum

def sumDiv3(number_list):
    div3_sum = 0
    for e in number_list:
        if e % 3 == 0:
            div3_sum += e
    return div3_sum


def replace(number_list):
    newlist = []
    for e in number_list:
        if e % 2 == 0:
            newlist.append(1)
        else:
            newlist.append(0)
    return newlist

def swap(number_list):
    if len(number_list) >= 2:
        temp = number_list[0]
        number_list[0] = number_list[-1]
        number_list[-1] = temp
    return number_list


def main():
    number_list = []
    print("Enter numbers on the same line:")
    numbers = input()
    numbers = numbers.split()
    for i in range(len(numbers)):
        number = int(numbers[i])
        number_list.append(number)

    even = evenNumbers(number_list)
    odd = sumOdd(number_list)
    div3 = sumDiv3(number_list)
    oneZero = replace(number_list)
    newlist = swap(number_list)

    print("List of even numbers:", even)
    print("Sum of odd:", odd)
    print("Sum of numbers divisible by 3:", div3)
    print("New list of 1s and 0s:", oneZero)
    print("List after replacing first with last:", newlist)

if __name__ == "__main__":
    main()
