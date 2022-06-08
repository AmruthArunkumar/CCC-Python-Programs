height = int(input())
width = int(input())
lines = int(input())
strokes = list(0 for _ in range(height + width)) # first rows, then columns
heightgold = 0
widthGold = list(0 for _ in range(width))
totalGold = 0

for i in range(lines):
    line = input().split()
    if line[0] == 'R':
        strokes[int(line[1]) - 1] += 1
    else:
        strokes[int(line[1]) - 1 + height] += 1

for i in range(len(strokes)):
    strokes[i] = strokes[i] % 2

    if strokes[i] > 0:
        if i < height:
            heightgold += 1
        else:
            widthGold[i - height] += height

for i in range(width):
    if widthGold[i] == height:
        totalGold += (height - heightgold)
    else:
        totalGold += heightgold

print(totalGold)