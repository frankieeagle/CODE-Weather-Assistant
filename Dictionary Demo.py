#declare dictionary

my_dictionary = {'jack': 111, 'mary': 190, 'sue': 878}
another_dict = {'first_name': 'Dallin', ''}


#access elements in a dictionary ( [], .get() )

print(my_dictionary['jack'])
my_dictionary['jack'] = 112
print(my_dictionary['jack'])

print(my_dictionary.get("jack"))

# Dictionary Loop
for bob in my_dictionary:
    print(f'{bob}: {my_dictionary[bob]}')