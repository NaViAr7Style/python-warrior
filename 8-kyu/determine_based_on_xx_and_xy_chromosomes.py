SON =       "Congratulations! You\'re going to have a son."
DAUGHTER =  "Congratulations! You\'re going to have a daughter."

def chromosome_check(chromosome):
    return SON if chromosome == "XY" else DAUGHTER