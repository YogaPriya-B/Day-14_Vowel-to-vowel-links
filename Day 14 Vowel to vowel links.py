str1=input()
l=str1.split(" ")
count=0
for i in range(0,len(l)-1):
    c=l[i]
    d=l[i+1]
    if(c[-1]=='a' or c[-1]=='e' or c[-1]=='i' or c[-1]=='o' or c[-1]=='u'):
        if(d[0]=='a' or d[0]=='e' or d[0]=='i' or d[0]=='o' or d[0]=='u'):
            count=count+1
if(count>0):
    print("True")
else:
    print("False")
    
