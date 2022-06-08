temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
k = temp[2]

start = 111

for x in range(2**n):
    for y in range(m):
