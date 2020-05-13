
# QUESTION

# Monk visits the land of Islands. There are a total of N islands numbered from 1 to N. Some pairs of islands are connected to each other by Bidirectional bridges running over water.
# Monk hates to cross these bridges as they require a lot of efforts. He is standing at Island #1 and wants to reach the Island #N. Find the minimum the number of bridges that he shall have to cross, if he takes the optimal route.
#
# Input:
# First line  contains two space-separated integers N, M.
# Each of the next M lines contains two space-separated integers X and Y , denoting that there is a bridge between Island X and Island Y.
#
# Output:
# Print the answer to each test case in a new line

def sort_path(am,n,f,s,iv):
    if(iv<n):
        for i in range(n):
            if(am[iv][i] == 1):
                if(f[i]!=-1):
                    if(s[i]==0):
                        s[i]=s[iv]+1
                    else:
                        if(s[i]>s[iv]+1):
                            s[i]=s[iv]+1
                    f[i] = -1
                else:
                    if s[i]+1<s[iv]:
                       s[iv]=s[i]+1
                       iv-=2
                        
        f[iv]=-1
        sort_path(am,n,f,s,iv+1)
    else:
        print(f"shortest path between land 1 and {n-1}=",s[n-1])
        return 0



N=int(input("enter the no. of lands"))

AM=[[0 for i in range(N)] for j in range(N)]
M=int(input("enter the total no. of bridges"))

print("enter the bridge relation between lands")

for i in range(M):
    n=int(input("enter first land"))
    m=int(input("enter second land"))
    AM[n-1][m-1]=1
    AM[m-1][n-1]=1


flag=[0 for i in range(N)]

path_sum=[0 for i in range(N)]

sort_path(AM,N,flag,path_sum,0)

