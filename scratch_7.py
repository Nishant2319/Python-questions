a=[[1,2],[34],[]]
for i in range(3):
    it = iter(a[i])
    for j in range(len(a[i])):
        print(next(it))


