b = []
def divid_Array(a,lb,ub):
    if lb < ub:
        mid=(lb+ub)/2
        divid_Array(a,lb,mid)
        divid_Array(a,mid+1,ub)
        merge_array(a,lb,mid,ub)


def merge_array(a,lb,mid,ub):
    i=lb
    j=mid+1
    while(i<=mid and j<=ub):
        if(a[i]<=a[j]):
            b.append(a[i])
            i+=1

        else:
            b.append(a[j])
            j += 1

    if(i>mid):
        while j<=lb:
            b.append(a[j])
            j+=1
    else:
        while i<=mid:
            b.append(a[i])
            i+=1




q=[2,7,5,9,2,3,7,4]
divid_Array(q,0,len(q)-1)
print(b)