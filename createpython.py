# in Excel, CONCATENATE(A1,",")
import os.path
list2 = ['DFS와 BFS'
,'바이러스'
,'미로 탐색'
,'토마토'
,'탈출'
,'동전 2'
,'알파벳'
,'트리의 부모 찾기'
,'빙산'
,'구슬 찾기'
,'줄 세우기'
,'장난감조립']

# define_type
ans1 = int(input('만들고 싶은 파일 유형(0 or 1)을 입력하세요 (Python : 0, Cpp : 1) : '))
option = ['py', 'cpp']  # 쓰는 언어 없으면 option에 추가하세여
lang = option[ans1]

# make_file
print('현재 경로: %s' % (os.getcwd()))
ans2 = int(input('만들고 싶은 경로가 맞습니까? (Yes : 0, No : 1) : '))
if(ans2 == 2):
    print('파이썬 코드를 원하는 경로에서 실행시켜 주세요')
else:
    for i in range(len(list2)):
        file_dir = str(os.getcwd() + "\%.1s_%s.%s" % (i+1, list2[i], lang))
        # print(file_dir)
        if(os.path.isfile(file_dir)):  # 이미 파일이 생성되어 있으면
            print('"%s.2_%s.%s" is exist' % (i+1, list2[i], lang))
        else:
            f = open("%02d_%s.%s" % (i+1, list2[i], lang), 'w')  # 파일이 없으면
            f.close()