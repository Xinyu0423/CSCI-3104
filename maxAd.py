import sys
import random
def maxAd(schoolTime):

    count=[];
    tempLength=len(schoolTime)
    while(len(schoolTime)!=0):
        earlistFinish = sys.maxsize
        for item in schoolTime:
            if(item[1] < earlistFinish):
                earlistFinish = item[1]
        count.append(earlistFinish)
        temp = []
        for item in schoolTime:
            if (item[0] <= earlistFinish):
                temp.append(item)
        for item in temp:
            schoolTime.remove(item)
    return count
def main():
    schoolPresent=[]
    #schoolPresent=[[5,73],[10,70],[10,98],[105,160],[130,186],[90,195]]
    for i in range(25):
        temp=random.randint(0,639)
        #temp is the start time, so it cannot equal to 640
        schoolPresent.append([temp, random.randint(temp+1, 640)])
        #beacuse the start time cannot equal to finish time, so we need to temp+1
    adTime=maxAd(schoolPresent)
    print(adTime)
if __name__ == '__main__':
    main()
