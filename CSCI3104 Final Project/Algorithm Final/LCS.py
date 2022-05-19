import random
def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    L = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena+1):
        for j in range(lenb+1):
            if i==0 or j==0:
                L[i][j]=0
            elif a[i-1]==b[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                # break ties
                #create a number randomly, then mod 2
                #if it is odd, choose to the top value
                #if it is even, choose the left value
                temp=(random.randint(0,100))%2
                if(L[i-1][j]==L[i][j-1]):
                    if(temp==1):
                        L[i][j]=L[i-1][j]
                    elif(temp==0):
                        L[i][j]=L[i][j-1]
                else:
                    L[i][j]=max(L[i-1][j], L[i][j-1])
    return L

inputFile=open("sequence_A.fa",'r');
stringA=''
firstLine=0;
for line in inputFile:
    line=line.replace(">","")
    line=line.replace("\n","")
    stringA=stringA+line;
#print(stringA)
inputFile=open("sequence_B.fa",'r');
stringB=''
for line in inputFile:
    line = line.replace(">", "")
    line = line.replace("\n", "")
    stringB=stringB+line;
#print(stringB)
inputFile=open("sequence_C.fa",'r');
stringC=''
for line in inputFile:
    line = line.replace(">", "")
    line = line.replace("\n", "")
    stringC=stringC+line;
#print(stringC)

ABResult=lcs(stringA,stringB);
ACResult=lcs(stringA,stringC);
BCResult=lcs(stringB,stringC);
ABLargest=0
ACLargest=0;
BCLargest=0;
for i in ABResult:
    #print(i)
    for j in i:
        if(j>ABLargest):
            ABLargest=j
for i in ACResult:
    #print(i)
    for j in i:
        if(j>ACLargest):
            ACLargest=j
for i in BCResult:
    #print(i)
    for j in i:
        if(j>BCLargest):
            BCLargest=j
print("the lcs result for AB is ",ABLargest)
print("the lcs result for AC is ",ACLargest)
print("the lcs result for BC is ",BCLargest)

