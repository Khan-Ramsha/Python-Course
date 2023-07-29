#Generators
def sqaure_num(num):
    for i in num:
        yield (i*i)   
snum = sqaure_num([1,2,3,4,5])

for n in snum:
   print(n)