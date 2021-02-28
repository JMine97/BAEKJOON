import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input().rstrip())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[0] * (26) for _ in range(26)]

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(n):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = input().split()
    a_ord = ord(a) - ord('a')
    c_ord = ord(c) - ord('a')
    graph[a_ord][c_ord] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(26):
    for a in range(26):
        for b in range(26):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for _ in range(int(input())):
    a, b, c = input().split()
    a_index = ord(a) - ord('a')
    c_index = ord(c) - ord('a')
    if graph[a_index][c_index] == 1:
        print('T')
    else:
        print('F')
