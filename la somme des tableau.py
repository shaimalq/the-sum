t1=[]
t2=[]
T=[]
n=int(input("veuilez saisir un nombre:"))
for i in range(1,n+1):
    print("t1[" ,i ,"]=",end=" ")
    t1.append(float(input()))
for j in range(1,n+1):
     print("t2[" ,j ,"]=",end=" ")  
     t2.append(float(input()))  
S=0
for i in range(1,n+1):
     for j in range(1,n+1):
        S=t1(i)+t2(j)
T.append(float(input()))
print(T)
