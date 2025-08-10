def divide(a, b):
    """Return quotient of a and b.

    Uses true division to preserve fractional results. Raises
    ZeroDivisionError if b is 0.
    """
    # Use true division; floor division would truncate the result.
    return a / b
