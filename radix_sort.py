from numpy import *

def find_digit(a):
     n=max(a)
     count=0
     while(n!=0):
         n//=10
         count+=1
     return count

def sort(a):
    n=find_digit(a)
    for i in range(n):
        b = []
        for l in range(10):
            b.append([])
        for j in range(len(a)):
            t=a[j]
            for k in range(i+1):
                q=t%10
                t=t//10
            b[q].append(a[j])
        k = 0
        for m in range(len(a)):
            if len(b[m])>0:
                it=iter(b[m])
                for b in range(len(b[m])):
                    a[k]=next(it)
                    k+=1




a=[4,2,8,199,9]
sort(a)
print(a)





