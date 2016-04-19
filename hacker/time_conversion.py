#! /bin/python


# time = raw_input().strip()
time = "07:05:45PM"
time = "12:40:22AM"
time = "12:40:22PM"
time = time.upper()

if len(time) < 2:
    print
else:
    if time[-2:] == "AM":
        if time[:2].isdigit():
            if time[:2] == "12":
                print "00" + time[2:-2]
            else:
                print time[:-2]
    elif time[-2:] == "PM":
        if time[:2].isdigit():
            bn = int(time[:2])
            bn = (bn + 12) % 24
            if bn == 0:
                print "12" + time[2:-2]
            else:
                print str(bn) + time[2:-2]
