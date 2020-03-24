def print_formatted(n):

    l = len(str(bin(n)[2:]))
    for i in range(1, n+1):
        d = str(i)
        o = str(oct(i)[1:])
        h = str(hex(i)[2:]).upper()
        b = str(bin(i)[2:])
        print d.rjust(l),o.rjust(l),h.rjust(l),b.rjust(l)
if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)