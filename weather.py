# Programmer: Corrigan Newsome
# Email: corrigannewsome@gmail.com
# Purpose: To convert tempatures from C to F and vice versa.

## Features used in the project.
# Loops
# Error Handling
# If statements
# Functions
# User input

while True:
    # Calculates C to F usiung functions
    def celciusToFahrenheit(C):
        F = round(C * (9 / 5) + 32)
        return F

    # Calculates F to C
    def FahrenheitToCelcius(F):
        C = round((F - 32) * 5 / 9)
        return C

    def goodbye():
        print("Thank you for using the tempature converter program")

    try:  # add error handling
        print("Welcome to the tempature converter.")
        # Take input from user.
        userInput = input("Is this temp Celsius or Farenheight? C/F: ")
        tempature = round(float(input("Please enter the tempature: ")))

        if userInput.lower() == "c":  # Using if statement
            celciusToFahrenheit(tempature)
            print(
                f"The temp you entered was {tempature} degrees Celcius, the temp in Farenheight is {celciusToFahrenheit(tempature)}"
            )
        elif userInput.lower() == "f":
            FahrenheitToCelcius(tempature)
            print(
                f"The temp you entered was {tempature} degrees Farenheight, the temp in Celcius is {FahrenheitToCelcius(tempature)}"
            )
        else:
            print("Incorrect Input")

    except (
        ValueError
    ):  # Catch error when a user enters a letter instead of a number for temp.
        print("Error, you must enter numeric values only")

    except Exception as exc:  # Catch any errors we may have missed.
        print(f"Error! {exc}")

    do_another = input("Do another (y/n)? ")
    if do_another.lower() != "y":
        goodbye()
        break