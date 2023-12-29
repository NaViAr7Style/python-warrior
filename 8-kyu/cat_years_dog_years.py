def human_years_cat_years_dog_years(human_years):
    return [human_years, pet_years(human_years, 4), pet_years(human_years, 5)]

def pet_years(human_years, one_year):
    years = 0

    while human_years > 0:
        if human_years > 2:
            years += one_year
        elif human_years > 1:
            years += 9
        else:
            years += 15
        human_years -= 1 

    return years

if __name__ == '__main__':
    print(human_years_cat_years_dog_years(1))