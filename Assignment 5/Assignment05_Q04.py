# Assignment05_Q04_part2

# Import isValid and area functions from MyTriangle module
from MyTriangle import isValid, area

def main():
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))
    
    valid = isValid(side1, side2, side3)
    
    if valid:
        triangle_area = area(side1, side2, side3)
        print(f"The area of the triangle is {triangle_area}")
    else:
        print("Input is invalid")

if __name__ == "__main__":
    main()
