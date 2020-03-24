inp = raw_input()
out = ""
for ch in inp:
    if ch.isupper():
        out+= ch.lower()
    else:
        out+=ch.upper()
print out