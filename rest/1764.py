import sys
input=sys.stdin.readline

a, b = map(int, input().split())
s_1=set()
s_2=set()

for _ in range(a):
    s_1.add(input().rstrip())

for _ in range(b):
    s_2.add(input().rstrip())

no=sorted(list(s_1 & s_2))

print(len(no))
for i in no:
    print(i)
