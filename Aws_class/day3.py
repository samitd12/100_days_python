#WAp to find area of the circle with radius 7.5, 8.97, 20.39,100,129,1600,1000,5.6,8.9,12.7,11.12,12.13
PI=3.14
def area(radius):
    return PI*radius*radius

numbers=[7.5, 8.97, 20.39,100,129,1600,1000,5.6,8.9,12.7,11.12,12.13]
for number in numbers:
    area_circle= area(number)
    print(f"Area oc circle with radius {number} is {area_circle}")

fruits =["Banana","Orange","Mango"]
for index,value in enumerate(fruits):
    print(index,value)

text="RAmayan"
for x in text:
    print(x)

tuple_example= (1,2,3,4,5)
for i in tuple_example:
    print(i)

li=[1,2,3,4,5,1,2,3]
print(set(li))

#Nested for loop

#Nested list, for matrix operation
a=[[1,1,1],[2,2,2],[3,3,3]]
print(a)
for i in range(0,3):
    for j in range(0,3):
        a[i][j]=1+a[i][j]
print(a)

for i in range(0,3):
    for j in range(0,3):
        a[i][j]=i+a[i][j]
print(a)

