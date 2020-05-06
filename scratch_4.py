//HEAP SORT 


def downheapify(a,n,i):
    l=i*2+1
    r=i*2+2
    flag=0
    if(l<=n):
        if(a[l]>a[i]):
            upheapify(a, l)
        downheapify(a,n,l)


    if(r<=n):
        if (a[r] > a[i]):
            upheapify(a, r) 
        downheapify(a, n, r)

def upheapify(a,i):
    p=(i-1)//2
    if(p>=0):
        if(a[p]<a[i]):
            temp = a[i]
            a[i] = a[p]
            a[p] = temp
        upheapify(a,p)
b=[2,8,1,3,9,12,10,5,7]
downheapify(b,len(b)-1,0)
print(b)
