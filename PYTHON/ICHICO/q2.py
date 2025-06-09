'''
0~9로 이루어진 문자열이 들어온다.
왼쪽부터 오른쪽으로 하나씩 확인하며 '곱하기' 혹은 '더하기' 연산으로 가장 큰 수를 만들라.
단, 연산은 왼쪽부터 순서대로 진행한다.
'''

data = input()

data = list(data)

print(data)
answer = int(data[0])

for i in range(1,len(data)):
    if data[i-1] == "0" or data[i-1] == 1:
        answer += int(data[i])
    else:
        answer *= int(data[i])

print(answer)
