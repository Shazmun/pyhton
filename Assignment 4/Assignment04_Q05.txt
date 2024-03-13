#Assignment04_Q05
#Define a function that takes parameter i, computes the sum of the series
def compute_series_sum(i):
    # Define the series
    series_sum = 0
    for n in range(1, i + 1):
        series_sum += n /  (n + 1)

    return series_sum
#Define a main function that calls the above function with values 1 to 20 
def main():
    print("i\tm(i)")
    for i in range(1, 21):
        series_sum = compute_series_sum(i)
        # Round the sum to four decimal places
        print(f"{i}\t{series_sum:.4f}")

if __name__ == "__main__":
    main()
