string=raw_input()
cnt=0
ab="abcdefghijklmnopqrstuvwxyz"
string=string.lower()
for i in ab:
    if(i not in string):
        cnt=0
    else:
        cnt+=1
if(cnt==26):
    print "yes"
else:
    print "no"
