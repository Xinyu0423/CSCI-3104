import random
def maxMin(arr):
    tempMax=0
    tempMin=0
    isEven=0
    if(len(arr)%2==0):
        if(arr[0]>arr[1]):
            tempMax=arr[0]
            tempMin=arr[1]
        else:
            tempMax=arr[1]
            tempMin=arr[0]
        isEven=1
    else:
        tempMax=arr[0]
        tempMin=arr[0]
        isEven=0
    if(isEven==1):
        for i in range(2, len(arr) - 1,2):
            if(arr[i+1]>arr[i]):
                if(arr[i+1]>tempMax):
                    tempMax=arr[i+1];
                if(arr[i]<tempMin):
                    tempMin=arr[i]
            elif(arr[i+1]<arr[i]):
                if(arr[i]>tempMax):
                    tempMax=arr[i]
                if(arr[i+1]<tempMin):
                    tempMin=arr[i+1]
    if (isEven == 0):
        for i in range(1, len(arr) - 1, 2):
            if (arr[i + 1] > arr[i]):
                if (arr[i + 1] > tempMax):
                    tempMax = arr[i + 1];
                if (arr[i] < tempMin):
                    tempMin = arr[i]
            elif (arr[i + 1] < arr[i]):
                if (arr[i] > tempMax):
                    tempMax = arr[i]
                if (arr[i + 1] < tempMin):
                    tempMin = arr[i + 1]
    return tempMax, tempMin

xArr=[]
yArr=[]
for i in range(0,50):
    randomX=random.randint(0,100)
    randomY=random.randint(0,100)
    xArr.append(randomX)
    yArr.append(randomY)
print("Values for x array")
print(xArr)
print("-----------------------------------------")
print("Values for y array")
print(yArr)
xMax,xMin=maxMin(xArr)
yMax,yMin=maxMin(yArr)
print("xMax=",xMax,"xMin=",xMin)
print("yMax=",yMax,"yMin=",yMin)
print("The coordinates for R is [",xMin,",", yMin,"]", "[",xMax,",",yMin,"]","[",xMin,",",yMax,"]","[",xMax,",",yMax,"]" )