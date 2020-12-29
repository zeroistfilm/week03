import sys
from collections import defaultdict,deque
sys.stdin = open("./seung/input.txt","r")
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
toy = [[] * (N+1) for _ in range(N+1)] # 장난감에 대한 2차원 배열을 만듬.
incoming_degree = [0 for _ in range(N+1)] # 진입차수 배열을 0~7까지 만듬.
tmp_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(M)] #인풋을 리스트로 받아옴.

print("토이:",toy)
for x, y, k in tmp_lst: #인접리스트를 리스트형태로 만듬. 리스트의 인덱스가 정점이고, 그 인덱스의 값이 정점과 인접한 정점들 표현.
    toy[x].append([y,k])
    print(f'토이 인덱스{x}에 {[y,k]} 넣기')
    incoming_degree[y] += 1
    print(f'진입 차수 배열 {y}에 1씩 추가')
print("가공한 후 toy:",toy)
que= deque([])
cnt = [ 0 for _ in range(N+1)] # 개수를 세는 배열?
print("cnt배열:",cnt)
print("진입차수:",incoming_degree)
for i in range(1,N+1): #1부터 N까지
    if incoming_degree[i] == 0: #진입차수가 0이면 큐에 넣기. 예시로 따지면 처음에는 7.
        que.append(i)
        cnt[i] = 1 #cnt 배열을 1로 하기?
print("cnt 배열(1로 세팅):",cnt)
while que:
    print("que 돌리기---")
    index = que.popleft() #큐에서 빼기
    print("인덱스:",index)
    print(f'toy[index]:{toy[index]}')
    for temp in toy[index]:
        print("temp:",temp)
        # for t in range(1,N+1): #cnt 2차원 배열을 탐색
            # print(f'cnt배열의 {t}행 {temp[0]}열 = {cnt[t][temp[0]]}이랑, {temp[1]} and {t}행 {index}열의 값 {cnt[t][index]}를 곱해서 더한다.')
        cnt[temp[0]] += (temp[1] * cnt[index])
        print("큐 중간에 cnt 배열:",cnt)
        incoming_degree[temp[0]] -= 1 # 그 정점에서 뿌리 내리는 지점의 전입차수를 -1 다 시킴(ex.7에서 6,5,4의 전입차수 다 -1 시킴)
        print("incoming_degree:",incoming_degree)
        print("인커밍 temp[0]번째:",incoming_degree[temp[0]])
        if incoming_degree[temp[0]] == 0:
            que.append(temp[0])
        print("큐:",que)
    print("que 돌리는 끝 부분 ---")

for i in range(1,N+1):
    if len(toy[i]) == 0:
        print("cnt배열:",cnt)
        print(i, cnt[i], sep=" ")
