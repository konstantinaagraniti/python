def String2ASCII(string):
    """
    A function for the convertion of a string to ASCII code.
    The function also checks if the ASCII number is prime.
    
    Arguments:
        string {string} -- The string to be converted to ASCII.
    
    Returns:
        number {integer} -- The ASCII number.
    """

    # Converting string to ASCII with ord
    # Initializing an empty number "string"
    number = ''
    # Loop to every character of the string
    for char in string:
        number += str(ord(char))

    # Converting number back to integer
    number = int(number)
    # If the number is <=1 then it is not a prime
    if (number <= 1):
        print ("String {} that converted to ASCII number {} is not prime.".format(string, number))
    else:
        # Starting a for loop from 2 to number-1 to check if there are any any positive divisors other than 1 and number itself.
        for i in range(2, number):
            # Checking if number is prime with modulo operator
            if (number % i == 0):
                print ("String {} that converted to ASCII number {} is not prime.".format(string, number))
                # Stopping the loop since a divisor is found.
                break
        else:    
            print(("String {} that converted to ASCII number {} is prime.".format(string, number)))
    
    return (number)


# Checking the function
if __name__ == "__main__":
    
    # Test 1
    string = "A"
    number = String2ASCII(string)
    
    # Test 2
    string = "a"
    number = String2ASCII(string)
   
    # Test 2
    string = "test"
    number = String2ASCII(string)
