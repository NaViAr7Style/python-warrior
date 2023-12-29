def find_multiples(x, y):
    return list([n for n in range(x, y+1) if not n % x])

## Note: This is also a possible solution
def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
