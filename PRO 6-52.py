w1,w2=map(int,raw_input().split())
x1,x2=map(int,raw_input().split())
y1,y2=map(int,raw_input().split())
z1,z2=map(int,raw_input().split())
if(w1==x1 and y1==z1 and w2==z2 and y2==x2):
  print "yes"
else:
  print "no"
