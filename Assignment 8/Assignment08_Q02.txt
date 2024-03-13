#Assignment08_Q02

def main():
    # Create dictionaries for room numbers, instructors, and meeting times
    room_numbers = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
    inst = {'CS101': 'haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': '1Burke', 'CM241': 'Lee'}
    time = {'CS101': '8:00 am', 'CS102': '9:00 am', 'CS103': '10:00 am','NT110': '11:00 am', 'CM241': '1:00 am'}
    

    # Get user input for course number
    course_number = input("Enter a course number: ")

    # Display infortion or show an error message
    if course_number in room_numbers:
        room_number = room_numbers[course_number]
        inst = inst[course_number]
        time = time[course_number]
        
        print(f"The details for course {course_number} are: ")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {inst}")
        print(f"Meeting Time: {time}")
    else:
        print(f"{course_number } is an invalid course number.")

if __name__ == "__main__":
    main()
