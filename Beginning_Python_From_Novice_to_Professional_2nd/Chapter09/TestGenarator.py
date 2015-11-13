def flattern(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested=[[1,2],[3,4],[5]]
for number in flattern(nested):
    print number

#

#
g=( (i+2)**2 for i in range(2,27))
print g.next()

h=sum(i**2 for i in range(2,27))
print h

def flattern_recursive(nested):
	try:
            for sublist in nested:
                print "sublist = ", sublist
                for element in flattern_recursive(sublist):
                    print "element = ", element
                    yield element
	except TypeError:
            print "nested = ", nested
            yield nested
	
#list_recursive=list( flattern_recursive( [[[1,2],3,4],5,6,[7,[8,[9,10]]]]) )
#print "list_recursive = ", list_recursive

flattern_recursive("test as a string")
#list_recursive2 = list(  )
#print "list_recursive2 = ", list_recursive2
