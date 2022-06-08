temp = list(map(int, input().split()))
n = temp[0]
w = temp[1]
d = temp[2]
paths = {}
for i in range(w):
    temp2 = list(map(int, input().split()))
    paths[temp2[0]] = temp2[1]
routes = list(map(int, input().split()))
swaps = []
for j in range(d):
    swaps.append(list(map(int, input().split())))

print("")

day = 0

def swap(routes, swaps, day):
    swap = swaps[day]
    swap[0] = swap[0] - 1
    swap[1] = swap[1] - 1
    temp = routes[swap[0]]
    routes[swap[0]] = routes[swap[1]]
    routes[swap[1]] = temp
    return routes

def getOptions(yI, tI, routes, paths):
    options = {"T":0, "P":0, "W":0}
    train = routes[tI]
    you = routes[yI]
    if tI != (len(routes) - 1):
        if you == train:
            options["T"] = 1
        if you in paths.keys():
            options["P"] = len(paths[you])
        if you in routes[(tI + 1):]:
            options["W"] = 1
    else:
        return -1
    return options

def considerTrain(yI, tI, routes, paths, goal, time):
    yI += 1
    tI += 1
    time += 1
    if routes[yI] == goal:
        return time
    else:
        options = getOptions(yI, tI, routes, paths)
        if options != -1:
            if options["T"] == 1:
                train = considerTrain(yI, tI, routes, paths, goal, time)

def considerWalk(yI, tI, routes, paths, goal, time):
    you = routes[yI]
    possible = paths[you]
    

for x in range(d):
    print("Day: " + str(day))
    yI = 2
    tI = 0
    routes = swap(routes, swaps, day)
    print(routes)
    for y in range(len(routes)):
        print("Train is at: " + str(routes[tI]))
        options = getOptions(yI, tI, routes, paths)
        print("-------")
        tI += 1
    day += 1
    print("")

