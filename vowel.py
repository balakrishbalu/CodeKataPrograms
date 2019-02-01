c=raw_input()
vowel=['a','e','i','o','u']
conso=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if c in vowel:
	print 'Vowel'
elif c in conso:
	print 'Consonant'
else:
	print "Invalid"
