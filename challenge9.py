
n = int(raw_input())
l = []
for i in range(0,n):
    t2 = raw_input()
    t1 = float(raw_input())
    l.append([t1,t2])
l.sort()
min1 = l[0][0]
min2 = 0
fl = False
for i in range(0,n):
    if l[i] [0] > min1 and fl == False:
        min2 = l[i][0]
        flag = True

    if l[i][0] == min2 and min2 > min1:
        print l[i][1]