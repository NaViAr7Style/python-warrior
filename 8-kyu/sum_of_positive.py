def positive_sum(arr):
    return sum([x for x in arr if x > 0])

## Other cool example
def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))