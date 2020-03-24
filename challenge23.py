def print_rangoli(size):

    l = [chr(i+97)  for i in xrange(size)]
    ll = []
    for i in range(size,0,-1):
        temp = l[i-1]
        for j in range(i,size):
            temp = l[j]+'-'+temp+'-'+l[j]
        ll.append(temp)

    for i in range(size,0,-1):
        print (i-1) * '--' + ll[size-i]+ (i-1)*'--'
        
    
    for i in range(size-1,0,-1):   
        print (size-i) * '--' +ll[i-1]+(size-i) * '--'
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)