inp=input()
arr=inp.split()
a=int(arr[0])
b=int(arr[1])
num=a
while True:
    if(num>b):
        break
    else:
        print(num,end='')
        if(num%2==1):
            num*=2
        else:
            num+=3