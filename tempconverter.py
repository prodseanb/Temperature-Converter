# Fahrenheit to Celsius = (F - 32) * .5556 = C
import sys

def try_again():
    again = input('Try again? Y or N: ')
    if again.upper() == 'Y':
        main()
    elif again.upper() == 'N':
        sys.exit()
    
def cel_to_fahr():
    val = float(input('Enter the Celsius value: '))
    result = (val * 1.8) + 32
    print(str(round(val)), "degrees Celsius = ", str(round(result)), "degrees Fahrenheit")
    try_again()
    
    
def fahr_to_cel():
    val = float(input('Enter the Fahrenheit value: '))
    result = (val - 32) * .5556
    print(str(round(val)), "degrees Fahrenheit = ", str(round(result)), "degrees Celsius")
    try_again()

        
def main():
    while True:
        try:
            print('\nTEMPERATURE CONVERTER (Fahrenheit to Celsius / Celsius to Fahrenheit)')
            pick = input('Choose the type of temperature scale to convert. Celsius or Fahrenheit. C or F: ')
            if pick.lower() == 'celsius' or pick.lower() == 'c':
               cel_to_fahr()  
            elif pick.lower() == 'fahrenheit' or pick.lower() == 'f':
               fahr_to_cel() 
   
        except Exception as e:
                    raise e

main()