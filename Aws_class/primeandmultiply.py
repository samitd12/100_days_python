def primenumber(a):
    if a<2:
        return False
    for number in range(2,int(a/2)+1):
        if a%number==0:
            return False
    else:
        return True



def multiplication_table(a):
        for i in range(1,11):
                multiply=a*i
                print(f"{a}*{i}={multiply}\n" )

# number =[5,10,17] 
# for x in range(0,3):                     
#     multiplication_table(number[x])
count = 0
sam=5
while count<20:
    if primenumber(sam):
        multiplication_table(sam)
        count=count+1
    sam=sam+1
    

