#! /bin/python


t = int(raw_input().strip())
ret = []
for a0 in xrange(t):
    n = int(raw_input().strip())

    x = -1
    y = -1

    for i in reversed(range(n / 3 + 1)):
        if (n - 3 * i) % 5 == 0:
            x = i
            y = (n - 3 * i) / 5
    if x == -1:
        ret.append("-1")
    else:
        one = ""
        for i in range(3 * x):
            one += "5"
        for i in range(5 * y):
            one += "3"
        ret.append(one)


for c in ret:
    print c
