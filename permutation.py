class PermutString:
    def __init__(self,n):
        self.string=n
        self.count=[]
        self.n=0

    def permutate(self):
        self.String=list(dict.fromkeys(self.string))
        for i in self.String:
            self.count.append(self.string.count(i))

        self.permutateuntil(self.count,[0 for i in range(len(self.string))],0)
    def permutateuntil(self,count,result,level):

        if(level==len(result)):
            self.printf(result)
            self.n+=1
        for i in range(len(self.String)):
            print(result,'     ',level)
            if(count[i]==0):
                continue
            result[level]=self.String[i]
            count[i]-=1
            self.permutateuntil(count,result,level+1)
            count[i]+=1
    def printf(self,a):
        s=''
        for i in a:
            s+=i
        print(s)

a=PermutString("nisahaa")
a.permutate()
print(a.n)