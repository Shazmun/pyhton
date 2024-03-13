import matplotlib.pyplot as plt

def main():
    # Get user input for city and year
    city = input("Enter city: ")
    year = input("Enter year: ")

    # Get average high temperatures for each month as a space-separated string
    temperature_input = input("Enter average high temperature for each month of the year: ")
    temperatures = [float(temp) for temp in temperature_input.split()]

    # Create a list of month names for labeling the x-axis
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Create the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(months, temperatures, marker='o', linestyle='-', color='b', linewidth=2)
    plt.title(f'{year} Average Monthly High Temperatures - {city} ')
    plt.xlabel('Months')
    plt.ylabel('Temperature')
    plt.grid(True)

    # Set Y-axis limits to start from 0
    max_temperature = max(temperatures)
    plt.ylim(0, max_temperature)

    # Show the graph
    plt.show()

if __name__ == "__main__":
    main()
