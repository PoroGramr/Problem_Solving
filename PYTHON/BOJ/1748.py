'''
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

'''

N = int(input())
answer = 0

# 입력 받은 N이 몇자리 수 인지 확인
length = len(str(N))

# N - 1 자리수 까지의 수의 길이 
lengthMinus = length - 1

for i in range(1, lengthMinus + 1):
    answer += (10**(i) - 10**(i-1)) * i


#  N 자리수의 길이
leftLength = N - 10 ** (length - 1)
answer += (leftLength + 1) * length
print(answer)

