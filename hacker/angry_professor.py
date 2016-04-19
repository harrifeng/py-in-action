#! /bin/python


t = int(raw_input().strip())

ret = []
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))
    cnt = 0

    for one in a:
        if one < 0:
            cnt += 1
    if cnt >= k:
        ret.append("NO")
    else:
        ret.append("YES")

for c in ret:
    print c
