#Assignment08_Q04
def main():
    # Create an empty dictionary to store country-capital pairs
    d = {}

    while True:
        # prompt the user for a county- captial 
        ask = input("Enter a country and a capital comma separated (Q to quit): ").strip()
        if ask.upper() == 'Q':
            break
        
        try:
            # Split the input into country and capital
            country, capital = map(str.strip, ask.split(','))
            # Add the country-capital pair to the dictionary
            d[country] = capital
        except ValueError:
            print("Invalid input. Please enter a valid country and capital.")
    #print the country-capital in table format
    print(f"\n{'COUNTRY':<15}{'CAPITAL'}")
    for country, capital in sorted(d.items()):
        print(f"{country:<15}{capital}")
        
if __name__ == "__main__":
    main()