def merge_the_tools(string, k):
    x = len(string)/k
    for i in range(0, len(string), k):
        str = string[i:i+k]
        c = ''
        for s in str:
            if s not in c:
                c += s
        print(c)
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    