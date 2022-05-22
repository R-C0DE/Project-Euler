limit=1000
largest_3=0
largest_5=0
largest_15=0
for i in range(limit-1, 0, -1):
    if i%3==0:
        largest_3=i
        break
for i in range(limit-1, 0, -1):
    if i%5==0:
        largest_5=i
        break
for i in range(limit-1, 0, -1):
    if i%15==0:
        largest_15=i
        break
print(largest_3,largest_5,largest_15)

def sumn( d, n):
    sumx=(n*(2*d+(n-1)*d))/2
    return int(sumx)
    
sum_3=sumn(3,largest_3/3)  
sum_5=sumn(5,largest_5/5)  
sum_15=sumn(15,largest_15/15)      
print(sum_3,sum_5,sum_15)
sum=sum_3+sum_5-sum_15
print(sum)
    
