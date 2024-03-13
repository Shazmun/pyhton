#Assignment07_Q02

import random

def data_file(file_name= "Salary.txt", lines=1000):
    ranks = ["assistant", "associate", "full"]
    with open(file_name, 'w') as file:
        for i in range(1, 1001):
            first_name = f"FirstName{i}"
            last_name = f"LastName{i}"
            rank = random.choice(ranks)
            if rank == "assistant": #in the range from 50,000 to 80,000
                salary = round(random.uniform(50000, 80000), 2)
            elif rank == "associate": #in the range from 60,000 to 110000
                salary = round(random.uniform(60000, 110000), 2)
            else:#in the range from 75,000 to 1,30,000
                salary = round(random.uniform(75000, 130000), 2)
            line = f"{first_name} {last_name} {rank} {salary}\n"
            file.write(line)

def salary_data(file_name="Salary.txt"):
    #initilized 
    assistant_total = 0
    associate_total = 0
    full_total = 0
    all_total = 0
    assistant_count = 0
    associate_count = 0
    full_count = 0
    all_count = 0

    with open(file_name, 'r') as file:
        for line in file:
            data = line.split()
            rank = data[2]
            salary = float(data[3])

            if rank == "assistant":
                assistant_total += salary
                assistant_count += 1
            elif rank == "associate":
                associate_total += salary
                associate_count += 1
            else:
                full_total += salary
                full_count += 1

            all_total += salary
            all_count += 1


    print(f"Total salary for assistant professors: {assistant_total:.2f}")
    print(f"Total salary for associate professors: {associate_total:.2f}")
    print(f"Total salary for full professors: {full_total:.2f}")
    #print(f"All Faculty: {all_total:.2f}")
    print(f"Average salary for assistant professors: {assistant_total / assistant_count:.2f}")
    print(f"Average salary for associate professors: {associate_total / associate_count:.2f}")
    print(f"FAverage salary for full professors: {full_total / full_count:.2f}")
    #print(f"All Faculty: {all_total / all_count:.2f}")


def main():
    #calls the above two functions.
    data_file()
    salary_data()

if __name__ == "__main__":
    main()
