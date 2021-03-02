import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a):
    a = find_parent(parent, a)
    b = a-1
    if b<0:
        return -1
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return 0

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v=int(input())
e=int(input())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

result=0
# Union 연산을 각각 수행
for i in range(e):
    a=int(input())
    if union_parent(parent, a)<0:
        break
    result += 1

print(result)
