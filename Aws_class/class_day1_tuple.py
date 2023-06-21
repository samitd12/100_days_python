# Instructions:
# Answer the following questions based on your understanding of tuples
# and their operations in Python.
# 1. Define a tuple named my_tuple with the following elements: 10,
# 20, 'a', 'b', True.
my_tuple =(10,20,'a','b',True)
# 2. Write the code to access and print the third element of the tuple
# my_tuple.
print(my_tuple[2])
# 3. Concatenate two tuples: tuple1 with elements (1, 2, 3) and tuple2
# with elements ('x', 'y', 'z'). Store the result in a new tuple called
# concatenated_tuple.
tuple1=(1,2,3)
tuple2=('x','y','z')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)
new_tuple=sorted(tuple1, reverse= True) #cannot use sort like in list need to use sorted
print(new_tuple)
print(type(new_tuple)) #when sorted it change into list
print(type(tuple(new_tuple))) #convert list into tuple by adding tuple infront
print(2 in tuple1)

count_1 =my_tuple.count(1) #to count number 1 in my_tuple
# 4. Write a Python code snippet to repeat the tuple my_tuple three
# times and store the result in a new tuple named repeated_tuple.
my_tuple =(1,2,3)
repeated_tuple = my_tuple*3
print(repeated_tuple)
# 5. Determine the length of the tuple concatenated_tuple using a
# built-in function and print the result.
print(len(concatenated_tuple))


"""for tuple to sort we use .sorted()"""