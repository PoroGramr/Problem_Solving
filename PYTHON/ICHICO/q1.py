'''
공포도가 높을수록 공포를 많이 느끼는 사람이다.

X 공포도를 가진 사람은 X 명 이상의 그룹에 속해야 그룹을 형성할 수 있다.

모험을 떠날 수 있는 최대 그룹수를 구하라 ( 단, 모든 사람이 그룹이 결성이 되지 않아도 된다.)

'''

n = int(input())

data = list(map(int, input().split()))
data.sort()

# 그룹의 수
result = 0

# 현재 그룹에 포함된 모험가의 수
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
