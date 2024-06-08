n=int(input())

for i in range(1,n+1):
    str_i=str(i)
    if(i%3==0 or str_i=='3'or str_i=='6'or str_i=='9'):
        print(0,'',end='')
    else:
        print(i,'',end='')