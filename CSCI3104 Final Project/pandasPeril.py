import random
def optimal(arr):
    size=len(arr)
    #print(size)
    if(size%2!=0):
        return 0
    #the size of the array have to be even
    solution=[[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(i,size):
            temp=j-i
            if(i>=2):
                #if it is comparing at least 3 numbers
                first=solution[temp+1][j-1]
                second=solution[temp][j-2]
                third=solution[temp+2][j]
                solution[temp][j]=max(arr[temp]+min(first,third),arr[j]+min(second,first))
            else:
                solution[temp][j]=max(arr[temp],arr[j])
    return solution[0][size-1]


'''arr=[4,2,10,5]
matrix=optimal(arr)'''
print("----------------First game:---------------")
size=random.randint(1,10)*2
arr=[]
sum=0
for i in range(size):
    temp=random.randint(1,10)
    sum=sum+temp
    arr.append((temp))
print(arr)
L=optimal(arr)
print("the result for greedy algorithm is ", sum-L)
print("the result for dynamic programming is ", L)

print("-------------------Second game--------------")
secondSize=random.randint(1,10)*2
secondArr=[]
secondSum=0
for i in range(secondSize):
    temp=random.randint(1,10)
    secondSumsum=secondSum+temp
    arr.append((temp))
print(secondArr)
secondL=optimal(secondArr)
print("the result for greedy algorithm is ", secondSum-secondL)
print("the result for dynamic programming is ", L)

