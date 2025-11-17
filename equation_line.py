import math
listx=[]
listy=[]
count=0
nvalues=int(input("Enter how many values you are going to enter"))
while count < nvalues:
    x=int(input("Enter an x value"))
    y=int(input("Enter an y value"))
    count+=1
    listx.append(x)
    listy.append(y)
   
x_mean=sum(listx)/count
print(x_mean)
y_mean=sum(listy)/count
newlistx=[]
newlisty=[]
for c in listx:
    newlistx.append(listx[c]-x_mean)
    print(newlistx)