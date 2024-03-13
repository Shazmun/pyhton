#Assignment06_Q07
import math  

def isMarkovMatrix(m):
    n = len(m)

    # Check if all elements are positive
    for i in range(n):
        for j in range(n):
            # If any element is negative, it's not a Markov matrix
            if m[i][j] < 0:
                return False  

    # Check if the sum of elements in each column is 1
    for j in range(n):
        column_sum = sum(m[i][j] for i in range(n))
        # If the column sum is not approximately 1, it's not a Markov matrix
        if not math.isclose(column_sum, 1.0, rel_tol=1e-9):
            return False  
     # All conditions met, it's a Markov matrix
    return True 

def main():
    # Prompt the user to enter a 3 by 3 matrix
    print("Enter a 3-by-3 matrix row by row:")
    matrix = []
    for i in range(3):
        # Get a row of values from the user as a string, split it into a list
        row = input().strip().split() 
        # Convert the values to floats and append them to the matrix
        matrix.append([float(x) for x in row])  

    # Check if it is a Markov matrix
    if isMarkovMatrix(matrix):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")
        
if __name__ == "__main__":
    main()  
