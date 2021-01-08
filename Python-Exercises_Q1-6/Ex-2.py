def bmi_calculator():

    #Calculates BMI

    height = float(input("Please enter your height in m: "))
    weight = float(input("Please enter your weight in kg: "))
    bmi = round(weight/(height**2),1)
    print ("Your bmi is " + str(bmi) + ".")
    if (bmi < 18.5):
        print ("You are underweight!")
    elif (18.5 <= bmi < 25.0):
        print ("Your BMI is normal.")
    elif (25.0 <= bmi < 30.0):
        print ("You are overweight!")
    else:
        print ("You are obese!")

bmi_calculator()