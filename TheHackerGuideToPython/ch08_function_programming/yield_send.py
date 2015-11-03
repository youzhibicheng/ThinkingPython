def shorten(string_list):
    length = len(string_list[0])
    #print "length = %d" % length
    for s in string_list:
        #print "for length = %d" % length
	length = yield s[:length]
	#yield s[:length]
        #print "for length = %d" % length
        

mystringlist = ['loremipsum', 'dolorsit', 'ametfoobarfoobar']
shortstringlist = shorten(mystringlist)
#print '1st'
#print shortstringlist.next()
#print '2nd'
#print shortstringlist.next()
#print '3rd'
#print shortstringlist.next()

result=[]
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
	number_of_vowels = len(filter(lambda letter: letter in 'aeiou',s))
  	print "s = %s" % s
	print "n = %d " % number_of_vowels
	# Truncating the next string depending
	# on the number of vowels in the previous one
	s = shortstringlist.send(number_of_vowels)
  	print "s1 = %s" % s
	result.append(s)
	print "result = %s" % result
except StopIteration:
    print "result2 = %s" % result
    pass
