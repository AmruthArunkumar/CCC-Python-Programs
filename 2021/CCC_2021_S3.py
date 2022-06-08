n = int(input())
p = []
w = []
d = []
for i in range(n):
    temp = list(map(int, input().split()))
    p.append(temp[0])
    w.append(temp[1])
    d.append(temp[2])

minC = min(p)
maxC = max(p)

def findT(n, p, w, d, c):
    t = 0
    for j in range(n):
        if p[j] < c:
            if p[j] < (c - d[j]):
                t += (w[j])*((c - d[j]) - p[j])
        elif p[j] > c:
            if p[j] > (c + d[j]):
                t += (w[j])*(p[j] - (c + d[j]))
    return t

def binarySearch(n, p, w, d, min, max):
    c = (min + max) // 2
    mid = findT(n, p, w, d, c)
    left = findT(n, p, w, d, c - 1)
    right = findT(n, p, w, d, c + 1)
    if left < mid:
        return binarySearch(n, p, w, d, min, c)
    elif right < mid:
        return binarySearch(n, p, w, d, c + 1, max)
    else:
        return mid

print(binarySearch(n, p, w, d, minC, maxC))