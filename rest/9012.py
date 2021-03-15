import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=list(input().rstrip())
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if stack[-1]=='(' and i==')':
                stack.pop()
            else:
                stack.append(i)
        print(stack)

    if len(stack)==0:
        print('YES')
    else:
        print('NO')