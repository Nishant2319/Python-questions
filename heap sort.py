def findPivot(a,lb,ub):
    p=a[lb]
    start=lb
    end=ub
    while start<end:
        while a[start]<=p and start<ub:
            start+=1
        while a[end]>p and end>lb:
            end-=1

        if start<end:
            temp=a[start]
            a[start]=a[end]
            a[end]=temp
    temp=a[end]
    a[end]=a[lb]
    a[lb]=temp
    return end
def sort_quick(a,lb,ub):
    if lb<ub:
        loc = findPivot(a, lb, ub)
        # print(loc)
        sort_quick(a, lb, loc - 1)
        sort_quick(a, loc + 1, ub)


f=[1,4,16,79,6,2,9,3,34]
sort_quick(f,0,len(f)-1)
print(f)