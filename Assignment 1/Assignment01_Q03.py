#Question 3

year = 365
hour = 24
minutes = 60
seconds = 60
seconds_per_year = year*hour*minutes*seconds
current_population = 312032486

births = 1/7 * seconds_per_year
deaths = 1/13 * seconds_per_year
immigrants = 1/45 * seconds_per_year

updated_population = births - deaths + immigrants

one_year = current_population + updated_population
two_year = one_year + updated_population
three_year = two_year + updated_population
four_year = three_year + updated_population
five_year = four_year + updated_population

print("population after one year: {:.0f}".format(int(one_year)))
print("population after two years: {:.0f}".format(two_year))
print("population after three years:{:.0f} ".format(three_year))
print("population after four years: {:.0f}".format(four_year))
print("population after five years: {:.0f}".format(five_year))
