
# You are given  queries. Each query is of the form two integers described below:
# - 1,x : Insert x in your data structure.
# - 2,y : Delete one occurence of y from your data structure, if present.
# - 3,z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:

# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: .

# Function Description

# Complete the freqQuery function in the editor below. It must return an array of integers where each element is a  if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

# freqQuery has the following parameter(s):

# queries: a 2-d array of integers
    
'''
def countFreq(mylist):
    ans = {}
    for i in mylist:
        if (i in ans):
            ans[i] +=1
        else:
            ans[i] = 1
    return ans
    
    
inL = []  
'''
ListOfOperation = [(1,1), (1,2), (1,2), (2,3), (1,1), (1,1), (3,2)]
ListOfOperation = [(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]
ListOfOperation = [(1,1), (1,2), (1,1), (3,1)]
ListOfOperation = [(1,1), (2,1),(2,1),(1,1),(3,1)]


ans = {}

def runQuery(op):
    i = op[1]
    operation = op[0]
    
    # 1
    if operation==1:
        if (i in ans):
            ans[i] +=1
        else:
            ans[i] = 1
        
    # 1
    if operation==2:
        if (i in ans and ans[i]>0):
            ans[i] -=1

    #print(ans, "  i  ",i) 
        
    # n --> 1 ???
    if operation==3:
        vals = list( ans.values() )
        #print(ans, "  i  ",i, "  vals  ", vals) 
        for ifreq in vals:
            if ifreq==i:
                return 1
        return 0
    
    return None

    
for op in ListOfOperation:
    #print(op)
    print( op, "  answer: ", runQuery(  op ) )
    
    

    
    '''
    
def runQuery(op):
    #numInsert = op[1]
    i = op[1]
    operation = op[0]
    #print(numInsert, operation)
    
    # 1
    if operation==1:
        #inL.append(numInsert)
        if (i in ans):
            ans[i] +=1
        else:
            ans[i] = 1
        
    # n -> 1 ???
    if operation==2:
        if (i in ans):
            ans[i] +=1
        #try:
        #    inL.remove(numInsert)
        #except:
        #    pass
    
    # n^2
    if operation==3:
        #vals = list( countFreq(inL).values() )
        vals = list( ans.values() )
        #print(  countFreq(inL) ," all values ", vals )
        for ifreq in vals:
            #print(ifreq ,  " f/i   ",  numInsert)
            if ifreq==i:
                return 1
        return 0
    
    return None

    
for op in ListOfOperation:
    #print(op)
    print( op, "  answer: ", runQuery(  op ) )
    
    
    
    '''
	
	
	
	============================================
	# Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

# name: a string.
# score: an integer.

# Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. If  or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns  -1 if a < b, 0 if a=b, and 1 if a > b.

# input=[
# ('amy', 100),
# ('david', 100),
# ('heraldo', 50),
# ('aakansha', 75),
# ('aleksa', 150)
# ]

# output=[
# ('aleksa', 150),
# ('amy', 100),
# ('david', 100),
# ('aakansha', 75),
# ('heraldo', 50)]
# ]

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
        
    def __repr__(self):
        return str({'name':self.name , 'score':self.score })
    
    def comparator(a, b):
        
        if a.score>b.score:
            return -1
        if a.score<b.score:
            return 1
        if a.name>b.name:
            return 1
        if a.name<b.name:
            return -1
        
        return 0
        
        
input=[
('amy', 100),
('david', 100),
('heraldo', 50),
('aakansha', 75),
('aleksa', 150),
('amy2', 220),
('david2', 50),
('heraldo2', 150),
('amy3', 10),
('david3', 300),
('heraldo3', 250)
]

        
input=[
('a', 100),
('b', 101),
('c', 101)
]

myinput = []
#for i in range(len(input)):
for i in input:
    name, score = i
    #print(name, score)
    xplayer = Player(name, score)
    myinput.append(xplayer)

#print(myinput)

output = sorted(myinput,key=cmp_to_key(Player.comparator))

print(output)
        
	
	