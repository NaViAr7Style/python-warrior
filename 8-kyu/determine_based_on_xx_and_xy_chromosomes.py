SON =       "Congratulations! You\'re going to have a son."
DAUGHTER =  "Congratulations! You\'re going to have a daughter."

def chromosome_check(chromosome):
    return SON if chromosome == "XY" else DAUGHTER

### Another cool solution, using formatting
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')
