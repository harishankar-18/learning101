for i in range(1,N,2): 
    print( int((M-i*3)/2)*"-" + i*".|." + int((M-i*3)/2)*"-" )
print( int((M-7)/2)*"-" + "WELCOME" + int((M-7)/2)*"-" )
for i in range(N-2,-1,-2): 
    print( int((M-i*3)/2)*"-" + i*".|." + int((M-i*3)/2)*"-" )
