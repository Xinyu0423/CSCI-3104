def Fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        previousNum=1
        preSecond=1
        temp=0
        for i in range(2,n+1):
            temp=previousNum+preSecond
            preSecond=previousNum
            previousNum=temp
        return temp

result=Fibonacci(423);
fiveNum= int(str(result)[:5])
print("result is ",result)
print("first five number is ", fiveNum)