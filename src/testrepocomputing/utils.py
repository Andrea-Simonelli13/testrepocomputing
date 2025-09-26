def square(x):
    """Return the square of a single number or a numpy array.

    Note by virtue of the ``2.`` (vs. ``2``) at the exponent, the output value
    is always a float, or an array of floats, even if the input is an integer
    (or an array of integers).

    Example
    -------

    >>> square(2)
    4.0
    >>> square(np.array([1, 2, 3]))
    array([1., 4., 9.])

    Arguments
    ---------
    x : array_like
        Input value(s) to be squared. This can be either a number (int or float)
        or a numpy array.

    Returns
    -------
    array_like
        The squared value(s) of the input.
    """
    return x**2.
