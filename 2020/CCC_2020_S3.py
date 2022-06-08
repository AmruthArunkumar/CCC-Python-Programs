import string

n = input()
h = input()

alphabet = list(string.ascii_lowercase)
nDict = {}
for char in alphabet:
    cc = n.count(char)
    if cc != 0:
        nDict[char] = cc

foundPerms = []
count = 0

if len(n) > len(h):
    print(0)
else:
    for i in range(len(h)):
        if h[i] in nDict.keys() and (i + len(n)) <= len(h):
            sub = h[i:(i + len(n))]
            subDict = {}
            for char in alphabet:
                subChar = sub.count(char)
                if subChar != 0:
                    subDict[char] = subChar
            isPerm = False
            if nDict.keys() == subDict.keys():
                isPerm = True
                for char in nDict.keys():
                    if nDict[char] != subDict[char]:
                        isPerm = False
            if isPerm and sub not in foundPerms:
                foundPerms.append(sub)
                count += 1
    print(count)
