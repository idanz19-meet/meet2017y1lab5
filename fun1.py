def add_numbers(c, end):
    start = c
    for n in range(start, end + 1):
        start = start + n
    return -(c - (start - 1) - 1)
