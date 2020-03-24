def split_and_join(line):
    line = line.split(' ')
    n = len(line)
    for i in range(0,n):
        print line[i]+'-'

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result