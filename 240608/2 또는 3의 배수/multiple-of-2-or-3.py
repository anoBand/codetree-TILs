n=int(input())

for i in range (1,n):
    if(i%2==0 or i%3==0):
        print('1 ',end='')
    else:
        print('0 ',end='')