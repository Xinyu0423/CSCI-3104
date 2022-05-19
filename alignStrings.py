
def alignStrings(x,y):
    S=[[0 for a in range(len(y)+1)] for b in range(len(x)+1)]
    #set all the elements of the matrix euqal to 0
    #the row and column is equal to len(x)+1 and len(y)+1

    for i in range(0, len(x)+1):
        for j in range(0, len(y)+1):
            if i==0:
                S[0][j]=j
            elif j==0:
                S[i][0]=i;
                #set the base case
            elif x[i-1]==y[j-1]:
                S[i][j]=min(S[i][j-1]+1, S[i-1][j]+1,S[i-1][j-1])
                #if characters are the same, find the min cost
            else:
                S[i][j]=min(S[i][j-1]+1, S[i-1][j]+1,S[i-1][j-1]+3, S[i-2][j-2]+5)
                #the minimun cost for swapping case
    return S

def extract(S,x,y):
    i= len(x)
    j= len(y)
    a=[[i,j]]
    while i>0 or j>0:
        if(S[i][j]-S[i-1][j-1]<3):
        #the indel case
            if S[i-1][j-1]==min(S[i-1][j], S[i][j-1],S[i][j],S[i-1][j-1]):
                if S[i-1][j-1]==S[i][j]:
                    #no operation case
                    a.insert(0,[i-1,j-1])
                    i=i-1
                    j=j-1
                else:
                    #because no operator cost is 2
                    #choose indel(insert or delete)
                    a.insert(0,[i,j-1])
                    j=j-1

            if S[i][j-1]==min(S[i][j], S[i-1][j],S[i][j-1]):
                a.insert(0, [i,j-1])
                j=j-1
            #insert case
            if S[i-1][j]==min(S[i][j], S[i-1][j],S[i][j-1]):
                a.insert(0, [i-1,j])
                i=i-1
                #delete case
        if (S[i][j] - S[i - 1][j - 1] ==3):
            a.insert(0, [i-1][j])
            i=i-1
            #if the value is 3 which means is sub case
        if (S[i][j] - S[i - 2][j - 2] == 5):
            a.insert(0,[i-2,j-2])
            i=i-2
            j=j-2
            # if the value is 5 which means is swap case
    return a
x="STEP"
y="APE"
result=alignStrings(x,y)
print(result)
extractResult=extract(result,x,y)
print(extractResult)