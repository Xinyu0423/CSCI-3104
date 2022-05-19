import re
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


def sumString(str):
    sum=0;
    listChar=["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    costChar=[]
    for i in range(1,27):
        costChar.append(i)
    # create a tempary list and store each cost in the cost char
    #correspond to each characters
    for i in range(len(str)):
        for j in range(len(listChar)):
            if(str[i]==listChar[j]):
                sum=sum+costChar[j]
    #calculate the sum
    return sum


def createList(nameList,line):
    temp=nameList
    tempList=[]
    random.shuffle(temp)
    #save the name list in a temp list
    #shuffle the temp list randomly
    #get the shuffle function from https://stackoverflow.com/questions/15511349/select-50-items-from-list-at-random-to-write-to-file
    for i in range(0,int(line/2)):
        tempList.append(temp[i])
    #get the first half of the array
    return tempList


def firstHash(halfList, firstHashList, firstHashColl):
    for i in range(0, len(halfList)):
        temp=sumString(halfList[i])%5701
        #sum mod l
        if(firstHashList[temp]==0):
            firstHashList[temp]=halfList[i]
        else:
            firstHashList[temp] = halfList[i]
            firstHashColl[temp]=firstHashColl[temp]+1
            #add the name to name list and record the collision
    return firstHashList, firstHashColl

def secondHash(halfList,secondHashList,secondHashColl):
    for i in range(0, len(halfList)):
        a=random.randint(0,5700)
        temp=(sumString(halfList[i])*a)%5701
        #(sum*a)mod l
        if(secondHashList[temp]==0):
            secondHashList[temp]=halfList[i]
        else:
            secondHashList[temp]=halfList[i]
            secondHashColl[temp]=secondHashColl[temp]+1
    return secondHashList,secondHashColl

def histogram(collisionList):
    plt.bar(range(len(collisionList)),collisionList,color="red")
    plt.title("collision result for hash function")
    plt.xlabel("Index for the array")
    plt.ylabel("Number of collision times")
    plt.show()

'''def firstChain(halfList, firstChainList):
    for i in range(0, len(halfList)):
        temp=sumString(halfList[i])%5701
        #sum mod l
        if(firstHashList[temp]):
            firstChainList[temp].append(halfList[i])
        else:
            firstChainList[temp].append([halfList[i]])
            #add the name to name list and record the collision
    return firstChainList

def secondChain(halfList,secondChainList):
    for i in range(0, len(halfList)):
        a=random.randint(0,5700)
        temp=(sumString(halfList[i])*a)%5701
        #(sum*a)mod l
        if(secondChainList[temp]==0):
            secondChainList[temp].append(halfList[i])
        else:
            secondChainList[temp].append([halfList[i]])
    return secondHashList,secondHashColl'''


inputFile=open("dist.all.last.txt")
nameList=[]
countLine=0
for line in inputFile:
    countLine=countLine+1
#get the number of lines in the file
inputFile=open("dist.all.last.txt")
for line in inputFile:
    temp=""
    for j in line:
        if(j.isalpha()==0):
            #strip off the non all non alpha string
            break
        temp = temp + j
    nameList.append(temp)
#print(nameList)

halfList=createList(nameList,countLine)
firstHashList=[0 for i in range(0,5701)]
firstHashColl=[0 for i in range(0,5701)]
#initialize firstHashList and firstHashColl to all 0
firstHashList, firstHashColl=firstHash(halfList,firstHashList,firstHashColl)
print("First hash list is")
print(firstHashList)
print("First hash collision is")
print(firstHashColl)
secondHashList=[0 for i in range(5701)]
secondHashColl=[0 for i in range(5701)]
#initialize secondHashList and secondHashColl to all 0
secondHashList,secondHashColl=secondHash(halfList,secondHashList,secondHashColl)
print("--------------------second hash function-------------------------")
print("second hash list is")
print(secondHashList)
print("second hash collision is ")
print(secondHashColl)
#print histograms
#histogram(firstHashColl)
#histogram(secondHashColl)
firstChainList=[[0 for i in range(5701)],[]]
secondChainList=[[0 for i in range(5701)],[]]
'''firstChainList=firstChain(halfList,firstChainList)
secondChainList=secondChain(halfList,secondChainList)
print(firstChainList)'''