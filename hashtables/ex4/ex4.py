def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    the_hash = {}
    result = []
    for x in a:
        abs_int = abs(x)
        if the_hash.get(abs_int) is not None:
            result.append(abs_int)
        else:
            the_hash[abs_int] = abs_int

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
