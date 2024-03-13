#Lab05
#part a
num1 = int( input ("Enter the first number: "))
num2 = int( input ("Enter second number; second number must be greater than the first number: "))
print()

#part b
count =0
if num1 % 2 == 0:
    counter = num1 + 1
else:
    count= num1
print(f"Odd integers between {num1} and {num2} are: ")
while count <= num2:
    print(count, end = " ")
    count = count + 2
print()

#part c   
if num1 % 2 == 0:
    counter = num1
else:
    count = num1 +1
sum_even= 0
while count <= num2:
    sum_even= sum_even + count
    count = count + 2
print(f"Sum of even integers between {num1} and {num2} = {sum_even}")

#part d
if num1 % 2 == 0:
    counter = num1 +1
else:
    count = num1 
sum_square_odd = 0
while count <= num2:
    sum_square_odd = sum_square_odd + count**2
    count = count + 2
print(f"Sum of the square of odd integers between {num1} and {num2} = {sum_square_odd}")
print()

#part e
t1= Number = "Number"
t2= Square_of_Number = "Square of Number"
print(f"{t1:<14s}{t2:<14s}")
count =1
while count <= 10:
    print(f"{count:<14d}{count*count:<14d}")
    count +=1








