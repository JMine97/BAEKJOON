import sys
from bisect import bisect_left
input=sys.stdin.readline

n=int(input())
st=list(map(int, input().split()))

number=[]
st.reverse()
number.append(st[0])

for i in range(1, len(st)):
    if number[-1]<st[i]:
        number.append(st[i])
    elif st[i]<number[-1]:
        idx=bisect_left(number, st[i])
        number[idx]=st[i]
    # print(number)
# print(number)
print(len(st)-len(number))