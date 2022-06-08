x = int(input())
same = {}
for i in range(x):
    temp = tuple(input().split())
    if temp[0] not in same.keys():
        same[temp[0]] = []
    same[temp[0]].append(temp[1])
y = int(input())
diff = {}
for i in range(y):
    temp = tuple(input().split())
    if temp[0] not in diff.keys():
        diff[temp[0]] = []
    diff[temp[0]].append(temp[1])
g = int(input())
groups = []
for i in range(g):
    groups.append(tuple(input().split()))

violated = 0
possible = x+y

for gr in groups:
    if possible == 0:
        break
    if gr[0] in diff.keys():
        for j in diff[gr[0]]:
            if j in gr:
                violated += 1
                possible -= 1
    if gr[1] in diff.keys():
        for j in diff[gr[1]]:
            if j in gr:
                violated += 1
                possible -= 1
    if gr[2] in diff.keys():
        for j in diff[gr[2]]:
            if j in gr:
                violated += 1
                possible -= 1
    if gr[0] in same.keys():
        for j in same[gr[0]]:
            if j not in gr:
                violated += 1
                possible -= 1
    if gr[1] in same.keys():
        for j in same[gr[1]]:
            if j not in gr:
                violated += 1
                possible -= 1
    if gr[2] in same.keys():
        for j in same[gr[2]]:
            if j not in gr:
                violated += 1
                possible -= 1

print(violated)
