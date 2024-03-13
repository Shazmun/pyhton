
def celsiusToFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

#method to convert fahrenheit to celsius 
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) *(fahrenheit - 32)
    return celsius

print(format("Celsius", "<15s"), format("Fahrenheit", "<15s"), "  |    ", format("Fahrenheit", "<15s"),format("Celsius", "<15s"))
print("-------------------------------------------------------------------------------")
                                       
celsius = 40
fahrenheit = 120
i=1

while i <= 10:
    print(format(celsius, "<15d"), format(celsiusToFahrenheit(celsius), "<15.2f"),"  |    ",
                                             format(fahrenheit, "<15d"), format( fahrenheitToCelsius(fahrenheit), "<15.2f"))
    celsius = celsius- 1
    fahrenheit =  fahrenheit- 10
    i+=1
