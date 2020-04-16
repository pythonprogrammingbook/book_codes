def add_two_numbers(a, b):
    """Add two numbers and 
       return the sum
    
    Parameters
    ----------
    a : [int or float]
        [Addand]
    b : [int or float]
        [Addand]
    """
    Sum = a + b  # addition

    return Sum

c = add_two_numbers(a=4, b=5)
print("The sum of {0} and {1} is {2}".format(4, 5, c))


