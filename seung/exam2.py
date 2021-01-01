import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")

N,K = map(int,sys.stdin.readline().split())

# 큐를 이용해 BFS로 풀기

queue = deque([[N,0]]) # 위치와 시간 넣기
visited = [0 for _ in range(200001)] # 위치의 방문 배열
options_list = [-1,1,2] # 걷기 혹은 순간이동

def solve():
    if K <= N: # 동생이 있는 위치가 점점 줄어드는 형태이면 -1의 반복만 가능
        time = N-K
        return time

    while queue:
        num,time = queue.popleft()
        if num == K:
            return time
        time+=1
        if num > 100001 or num < 0:  # 위치가 10만 까지이므로 10만 넘어가면 큐에 넣는거 불필요
            continue
        for index in range(len(options_list)):
            if index == 2: # 곱하기는 예외
                location = num * options_list[index]
            else:
                location = num + options_list[index]
            if visited[location] == 0:
                queue.append([location,time])
                visited[location] = 1

print(solve())
