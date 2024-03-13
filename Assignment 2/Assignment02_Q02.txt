#Question 2
#prompts the user enter weight and price gor both packages
weight_1= float(input("Enter weight for package 1:") )
price_1= float(input("Enter price for package 1: ") )
weight_2= float(input("Enter weight for package 2: ") )
price_2= float(input("Enter price for package 2: ") )

package_1 = price_1 / weight_1
package_2 = price_2 / weight_2

# use if statement 
if package_1  < package_2 :
    print("Package 1 has the best price.")
elif package_1  > package_2 :
    print("Package 2 has the best price.")
else:
    print("Package 1 and Package 2 have the same price.")
