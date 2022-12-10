i = 1 # While variable

#Fizz and Buzz variables, in case they want to be changed quickly
f = 3
b = 5

while i <= 100:

    if (i % f == 0) & (i % b == 0): # FizzBuzz condition
        print("FizzBuzz")
    
    elif i % f == 0: # Fizz condition
        print("Fizz")
    
    elif i % b == 0: #Buzz condition
        print("Buzz")
    
    else: # If no conditions trigger, prints the number
        print(i)
    
    i = i + 1