n = int(raw_input())
arr = {}
for i in range(n):
    (name, m1, m2, m3) = raw_input().split(' ')
    m1 = float(m1)
    m2 = float(m2)
    m3 = float(m3)
    arr[name] = (m1+m2+m3)/3
name = raw_input()
print arr[name]