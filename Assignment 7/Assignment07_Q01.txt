#Assignment07_Q01

def main():
    # Prompt the user to enter the filename
    file_name = input("Enter the filename: ")


    # Open the file and read the scores
    with open(file_name, 'r') as file:
        scores = [int(score) for score in file.read().split()]
        

    # Display the list of scores
    print(f"{scores}")

    # Calculate the number, total,  and average
    num_scores = len(scores)
    print(f"There are {num_scores} scores ")

    total_scores = sum(scores)
    print(f"The total is {total_scores}")

    avg_score = total_scores / num_scores
    print(f"The average is {avg_score:.2f}")

   
if __name__ == "__main__":
    main()
