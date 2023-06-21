#WAP to show usecase of function with combination of return and agrument.

#no return no agrument
# def chocolate():
#     print("No return no agrument")

# chocolate()

#no return with agrument
# def banana(a):
#     print(f"{a} is the agrument here")

# banana(5)

# #return without agrument
# def apple():
#     return 55

# print(apple())

# #return and agrument
# def pineapple(a,b,c=1):
#     return a+b+c
# print(f"the sum is {pineapple(5,6)}")

#WAp to print even number between 2 and 50 also perform the addition of those even number
# sum=0
# for x in range(2,51):
#     if x%2 == 0:
#         print(x)
#         sum += x
# print(sum)

#WAp to print odd number between 2 and 50 also perform the addition of those even number
# sum=0
# for x in range(2,50):
#     if x%2 == 0:
#         print(x+1)
#         sum += x+1
# print(sum)


#WAp to print prime number between 2 and 100 and perform the addition.

def primenumber(a):
    if a<2:
        return False
    for number in range(2,int(a/2)+1):
        if a%number==0:
            print(f"{a} is not a prime")
            break
    else:
        print(f"{a} is a prime")

for x in range(4,100):
    primenumber(x)

#Another method
# def check_prime(a):
#     for i in range(2, int(a/2)+1):
#         if a%i==0:
#             print("not prime")
#             return False
#     return True
# if chcek_prime(10):
#     print("prime")    

#WAP to give the multiplication table of 5,10,17
# def multiplication_table(a):
#         for i in range(1,11):
#                 multiply=a*i
#                 print(f"{a}*{i}={multiply}\n",a*i )

# number =[5,10,17] 
# for x in range(0,3):                     
#     multiplication_table(number[x])
