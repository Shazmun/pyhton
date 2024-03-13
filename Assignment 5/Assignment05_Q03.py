# Assignment05_Q03

# Define the falling_distance function that calculates the distance
def falling_distance(t):
    g = 9.8  
    # Calculate the distance using the formula
    distance = 1/2 * g * t**2  
    return distance  


def main():
    # Print the table header
    print("Time\t\t\tFalling Distance") 
    print("-------------------------------------")
    # Loop through time intervals from 1 to 10 seconds
    for t in range(1, 11): 
        distance = falling_distance(t)  
        print(f"{t}\t\t\t{distance:.2f}")  

if __name__ == "__main__":
    main()
