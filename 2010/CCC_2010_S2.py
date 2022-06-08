n = int(input())
letters = {}
for i in range(n):
    temp = list(input().split())
    letters[temp[1]] = temp[0]
sequence = input()

start = 0
end = 1
last = len(sequence) - 1
encoded = ""

while start <= last:
    while sequence[start:end] not in list(letters.keys()):
        end += 1
    encoded += letters[sequence[start:end]]
    start = end
    end = start + 1

print(encoded)