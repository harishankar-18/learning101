def count_substring(string, sub_string):
    r = 0
    for i in range (len(string)-len(sub_string)+1):
        if sub_string == string[i:i+len(sub_string)]:
            r= r+ 1
    return r

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count