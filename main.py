# Task nr.1
  
# User enters two names separated by comma : 
# for example :('Mindaugas PiktasDestytojas, Mindaugas Juokauja') 
# Create a function that would swipe surnames and will prduxe new name surname 
# and another function funtion that will swap names.


# def swipe_surname(name_surname):
#     return name1 + name2
# names = name_surname.split(', ')

# def swipe_name(name1, surname2):
#     return surname1 + surname2

user_input = input("Enter two names separated by commas: ")

def swap_surnames(names):
    return ', '.join(reversed(names.split(', ')))

def swap_names(surnames):
    first_name, last_name = surnames.split(', ')
    return f"{last_name}, {first_name}"

full_name = user_input
swapped_surnames = swap_surnames(full_name)
swapped_names = swap_names(full_name)

print(swapped_surnames)
print(swapped_names)