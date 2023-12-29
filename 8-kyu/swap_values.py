def swap_values(args): 
    temp = args[0]
    args[0] = args[1]
    args[1] = temp

## Other possible solution
def swap_values(args): 
    args[0], args[1] = args[1], args[0]