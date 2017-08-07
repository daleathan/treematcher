from treematcher import TreePattern
from ete3 import Tree, PhyloTree

t = Tree("(((((A, A2, A3), B), (C,D)), E), F);") 

print "Example 1"
# This should not give a match (as we search for a very strict pattern), but it does
p = TreePattern("(A,A2);")
for m in p.find_match(t):
    print m

print "Example 2"
# This should be possible, and then match any node like (A, A2, A3, ...)
try:
    p = TreePattern("(A,A2,*);")
    for m in p.find_match(t):
        print m
except Exception, e:
    print "Error in example", e


print "Example 3"
# This is perfect behaviour (if not yet, example should be a test case)
p = TreePattern("((A,A2,A3)*, E);")
for m in p.find_match(t):
    print m
    
print "Example 4"
# This is perfect (if not yet, example should be a test case)
p = TreePattern("((A,A2,A3)*, B);")
for m in p.find_match(t):
    print m
    

print "Example 5"
# Would be nice to implement dot symbol as node of any name (like in perl RE)
p = TreePattern("((A,A2,A3), (C,.));")
for m in p.find_match(t):
    print m
    
    
print "Example 6"
# This is perfect (if not yet, example should be a test case)
p = TreePattern("(((A,A2,A3)*, (C,D))*, F);")
for m in p.find_match(t):
    print m


print "Example 7"
# Expected a match, but none is reported  
p = TreePattern("((A,A2,A3){2}, (C,D));")
for m in p.find_match(t):
    print m
    
    
print "Example 8"
# works as expected, should be a test case
p = TreePattern("((A,A2,A3){1}, B);")
for m in p.find_match(t):
    print m

    