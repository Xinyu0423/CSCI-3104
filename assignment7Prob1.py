import random
#get all merge sort implementation online
def mergeSort(myList):
    count = 0
    #print("Splitting ",myList)
    #print("count= ",count)
    if len(myList)>1:
        mid = len(myList)//2
        left = myList[0:mid]
        right = myList[mid:len(myList)]

        count=mergeSort(left)
        count=count+mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k]=left[i]
                i=i+1
            else:
                myList[k]=right[j]
                j=j+1
                count=count+(len(left)-i)
            k=k+1
        while i < len(left):
            myList[k]=left[i]
            i=i+1
            k=k+1
        while j < len(right):
            myList[k]=right[j]
            j=j+1
            k=k+1
    return count

myList=[]
i=0
for i in range (100):
    temp=random.randint(0,1000)
    myList.append(temp)
count=0
print("before sorting:")
print(myList)
print("-----------------------------------------")
count=mergeSort(myList)
print("after sorting")
print(myList)
print("count is ",count)
