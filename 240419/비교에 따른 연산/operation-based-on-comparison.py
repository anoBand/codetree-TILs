ss=input()
num1, num2 = map(int, ss.split())
if num1>num2:
    print(num1*num2)
else :
    print(num2//num1)