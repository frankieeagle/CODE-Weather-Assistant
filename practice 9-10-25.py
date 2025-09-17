#declare a list

my_list = ["banana", "apple", "orange"]
int_list = [1,2,3,4]
mixed_list = [1, 9.9, True, "Blue"]
empty_list = []

#acess list elements

print(my_list[0])
print(my_list[1])

my_list[1] = "peach"

#add elements to list (append())

empty_list.append("not empty anymore")
print(empty_list)
print(empty_list[0])
my_list.append('orange')

#list.count()

print(my_list.count('orange'))
print(my_list.count('peach'))


#removing from a list (del)

del my_list[1]
del my_list[0]
print(my_list)
print(my_list[1])


#list.remove()
print(my_list)
my_list[0] = "orange"
my_list.remove("orange")
print(my_list)

# Deep vs shallow copies

new_int_list = int_list   #deep copy
newer_int_list = int_list.copy()
print(int_list)
print(new_int_list)

int_list[0] = "turtle"

print(int_list)
print(new_int_list)
print(newer_int_list)


# print(int_list)
# print(int_list_2)
# print(int_list_3)


# Iterating over a list

for num in int_list:
    print(f"Here's a number: {num}")


#declare a tuple

int_tuple = (1, 2, 3)

# Access an elemnt in a tuple

print(int_tuple[0])
print(int_tuple[1])
print(int_tuple[2])

# modify a tuple

#int_tuple[0] = 99  #Cant change, immutable
print(int_tuple)


for i in range(100):
    print(i)
