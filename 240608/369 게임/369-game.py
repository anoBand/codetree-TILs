n=int(input())

for i in range(1,n+1):
    str_i=str(i)
    if( '3' in str_i or '6' in str_i or '9' in str_i):
        print(0,'',end='')
    else:
        print(i,'',end='')