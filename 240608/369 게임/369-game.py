# 숫자를 입력받는다.
number = input("숫자를 입력하세요: ")

# 숫자에 '1', '2', '3' 중 하나라도 포함되어 있는지 확인한다.
if '1' in number or '2' in number or '3' in number:
    print(0)
else:
    print(number)