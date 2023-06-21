for i in range(20,30):
    prime=1
    for j in range(2,int(i/2)+1):
        if i%j == 0:
            prime = 0
            print(i,"not prime")
            break
    if prime==1:
        print(i,"Prime number")

"""Different method"""
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
