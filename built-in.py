import math
import time
#task1
x=[5,4,3,2,76,8]
res=math.prod(x)
print(res)
#task2
text="LalalaYYggbN"
up=sum(1 for i in text if i.isupper())
low=sum(1 for i in text if i.islower())
print("Uppercase:",up)
print("Lowercase:",low)
#task3
a=input("etner word:")
if a==a[::-1]:
    print("yes")
else:
    print("no")
#task4
numb=int(input("number:"))
timer=int(input("milisec:"))
time.sleep(timer/1000)
res=math.sqrt(numb)
print(f"Square root of {numb} after {timer} miliseconds is {res}")
#task5
y=(True,5,"bbbb")
print(all(y))