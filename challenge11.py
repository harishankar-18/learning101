import numpy
x = list(map(int,raw_input().split()))
N = x[0]
M = x[1]
l = []
for i in range(N):
    a= list(map(int,raw_input().split()))
    arr= numpy.array(a) 
    l.append(arr)
print numpy.mean(l, axis = 1)
print numpy.var(l, axis = 0)
print numpy.std(l, axis = None)