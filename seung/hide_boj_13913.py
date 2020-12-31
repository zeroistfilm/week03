import sys
from collections import deque
sys.stdin = open("./seung/input.txt","r")
N,K = map(int,sys.stdin.readline().split())

op_lst = [-1,1,2]

que = deque([[N,0]])
visited= [0 for _ in range(100001)]
path = [0 for _ in range(100001)]
def solve():
    if K<= N: # k가 n보다 작다면, 감소하는건 여기서 바로 처리.(n-k가 최소거리임.)
        print(N-K)
        for i in range(N,K-1,-1):
            print(i, end=" ")
        return
    while que:
        num,time = que.popleft()
        if num == K:
            print(time)
            p = []
            temp = num
            for _ in range(visited[num]+1): # 트리의 부모 찾는 로직으로 응용해보자.
                p.append(temp)
                temp = path[temp]
            p.reverse()
            print(*p)
            return
        time+=1
        if num > 100000 or num < 0: # 시간 단축, num이 10만 넘어가면 굳이?, 0 미만은 위에서 거른다.
            continue
        for index in range(len(op_lst)):
            if index == 2:
                result = num * op_lst[index]
            else:
                result = num + op_lst[index]

            # print("visited,result",result, time)
            if 0 <= result < 100001 and visited[result]== 0:
                que.append([result,time])
                path[result]= num
                visited[result]= visited[num]+1
solve()


