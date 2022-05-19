def findMin(A,length):
    if length==1:
        return A[0]
    minP=findMin(A,length-1)
    if A[length-1]<minP:
        return A[length-1]
    else:
        return minP

def maxPF(A,minP,maxP,i):
    minP=findMin(A,i+1)
    currMaxP=A[i]-minP
    #print("currMaxP= ",currMaxP)
    #print("A[i]is", A[i])
    i+=1
    if(i>len(A)-1):
        return maxP
    elif currMaxP>maxP:
        maxP=currMaxP
    return maxPF(A,minP,maxP,i)

#def main():
    myList=[2,5,1,3,2]
    size=len(myList)
    #print(size)
    minPF=findMin(myList,size)
    print("Smallest element in the array is ",minPF)
    maxP=maxPF (myList,minPF,0,0)
    print("Max profit is",maxP)
#if __name__ == '__main__':
#    main()
