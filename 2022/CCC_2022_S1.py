n = int(input())

if n <= 3:
    print(0)
elif n <= 5:
    print(1)
else:
    count = 0
    for i in range(int(n/5) + 1):
        val = n - (5 * i)
        if val % 4 == 0:
            count += 1
    
    print(count)