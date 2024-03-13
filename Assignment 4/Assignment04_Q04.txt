#Assignment04_Q04

# Define a function that converts milliseconds to hours, minutes, and seconds
def convertMillis(millis):
    # Calculate total seconds
    total_seconds = millis / 1000

    # Calculate hours, minutes, and seconds
    hours = int(total_seconds // 3600)
    remaining_seconds = total_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)

    return hours, minutes, seconds

# Define a main function that prompts the user to enter a value for milliseconds
def main():
    millis = int(input("Enter time in milliseconds: "))
    hours, minutes, seconds = convertMillis(millis)

    # Display the result in the format of hours:minutes:seconds
    print(f"{hours}:{minutes}:{seconds}")

if __name__ == "__main__":
    main()
