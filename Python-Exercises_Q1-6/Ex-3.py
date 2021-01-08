def celsius_to_fahrenheit():

    #Converts temperature from celsius to fahrenheit

    celsius = float(input("Please enter the temperature in celsius: "))
    fahrenheit = (celsius * (9/5)) + 32
    print ("The temperature in celsius is " + str(celsius) + ". The temperature in fahrenheit is " + str(fahrenheit) + ".")

celsius_to_fahrenheit()