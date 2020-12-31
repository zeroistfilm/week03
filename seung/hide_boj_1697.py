import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")
N,K = map(int,sys.stdin.readline().split())

op_lst = [-1,1,2]

que = deque([[N,0,0]])
visited= [0 for _ in range(100001)]
def solve():
    if K<= N: # k가 n보다 작다면, 감소하는건 여기서 바로 처리.(n-k가 최소거리임.)
        print(N-K)
        return
    while que:
        num, i,time = que.popleft()
        time+=1
        if num > 100000 or num < 0: # 시간 단축, num이 10만 넘어가면 굳이?, 0 미만은 위에서 거른다.
            continue
        for index in range(len(op_lst)):
            if index == 2:
                result = num * op_lst[index]
            else:
                result = num + op_lst[index]
            if result == K:
                break
            # print("visited,result",result, time)
            if result != N and visited[result]==0:
                que.append([result,index,time])
                visited[result]=1
        if result == K:
            print(time)
            break

solve()
# 100|0 반례를 넣으니까 100번까지는 돌아야 하는데 visited 숫자를 주어버리니까 인덱스가 더 이상 안 돌아감. in visited로 가야하는 것 같다.


