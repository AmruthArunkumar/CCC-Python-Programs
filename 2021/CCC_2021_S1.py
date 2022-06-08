import math

pieces = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))
area = 0

for i in range(pieces):
    area += widths[i] * (heights[i] + heights[i + 1]) / 2

if area % 1 != 0.5:
    area = int(area)

print(area)
