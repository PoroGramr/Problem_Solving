'''
수빈이는 현재 N 에 위치, 동생은 점 K에 위치한다.

수빈이는 1초후에 X - 1 혹은 X + 1로 이동하거나
순간이동을 하는 경우에는 0초후에 2 * X 의 위치로 이동할 수 있다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇초 후 인가?

'''
from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)


limit = 100000
v = [-1 for _ in range(100001)]
v[N] = 0
answer = 0


while q:
    cur = q.popleft()

    if cur == K:
        answer = v[cur]
        break

    jump = cur * 2
    left = cur - 1
    right = cur + 1

    if 0 <= jump and jump <= limit and v[jump] == -1:
        q.append(jump)
        v[jump] = v[cur]

    if 0<= left and left <= limit and v[left] == -1:
        q.append(left)
        v[left] = v[cur] + 1
    
    if 0 <= right and right <= limit and v[right] == -1:
        q.append(right)
        v[right] = v[cur] + 1




print(answer)
