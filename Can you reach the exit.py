## Reach N-1 N-1
## https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python
## 4 kyu

import time
def path_finder(maze):
    steps = [(0, 1), (1, 0),(0,-1),(-1,0)]
    start = (0,0)
    ox = []
    oy = []
    x = 0
    y = 0
    queue = [start]
    discarded = []

    for i in range(len(maze)):
        if maze[i] is 'W':
            ox.append(x)
            oy.append(y)
        if maze[i] is "\n":
            y += 1
            x = 0
        else:
            x += 1
    n = x
    borders = [n, n]

    while queue:
        current = queue[len(queue) - 1]
        queue.pop(len(queue) - 1)
        if current == (n - 1, n - 1):
                return True
        for i in steps:
            neighbor = (current[0] + i[0], current[1] + i[1])
            if not ((neighbor[0], neighbor[1]) in zip(ox, oy)):
                if (neighbor[0], neighbor[1]) not in discarded:
                    if (0 <= neighbor[0] <= borders[0]-1) and (0 <= neighbor[1] <= borders[1]-1):
                        if neighbor not in queue:
                            queue.append(neighbor)

        discarded.append(current)
    return False

startt = time.time()
b = "\n".join([
    ".W......................",
"........................",
".W......................",
".W......................",
".W......................",
".W......................",
".W..........W...........",
".W..........W...........",
".W..........W...........",
".W..........W...........",
".W..........W...........",
".W..........W.W.........",
".W..........W.W.........",
".W..........W...........",
".W..........W...........",
".W..........W...........",
".W..........W...........",
".W........WW............",
".W..................W...",
".W..........WWWWWWWW.....",
".W..............W..W....",
".W.................W....",
".W.................W....",
".W.............W...W....",
".W.................W....",

])
a = "\n".join([
    ".W.",
    ".W.",
    "..."
])
e = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

print(path_finder(b))

end = time.time()
print(end - startt)









