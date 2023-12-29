def evil(n):
    initial = bin(n).count('1')
    less = bin(n).replace('1', '')

    count = len(initial) - len(less)

    mindset = "Evil" if not count % 2 else "Odious"
    return "It's {}!".format(mindset)

## Another great solution
def evil(n):
    return 'It\'s {}!'.format(('Evil', 'Odious')[bin(n).count('1') % 2])