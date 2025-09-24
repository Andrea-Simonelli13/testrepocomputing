def square_bin(a,b):
    """Return the square of a sum or a difference between two number using the binomial square formula.
    
       Example
       -------

       >>> square_bin(2, -3)
       1.0
       >>> square_bin(2, 3)
       25.0
    """
    bin = (a*a)+(2*a*b)+(b*b)
    return bin