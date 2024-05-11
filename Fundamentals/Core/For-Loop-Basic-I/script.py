for i in range (0,150):
    print(i+1)

for i in range (0,1000,5):
    print(i+5)

for i in range (1,101):
    if  i%5==0 and not i%10==0:
        print("Coding") 
        continue
    if i%10==0 and i%5==0:
        print("Dojo") 
    else : 
        print (i)

a = 0
b = 500
result=0

for i in range (a,b):
    if not i%2==0:
        result+=i
print(result)

for i in range (2018,0,-4):
    print(i) 

lownum=2
highnum=9
mult=3

for i in range (lownum, highnum+1):
    if i % mult == 0:
        print (i)
