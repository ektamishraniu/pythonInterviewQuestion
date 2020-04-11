Given a list of intervals, return a list of non-overlapping intervals.
If intervals are overlapping, merge them.
E.g., [6, 9], [1, 4], [3, 5], [8, 12] -> [1, 5], [6, 12]

(Notes)
(1) boundaries are included;
(2) multiple intervals can be overlapping;
(3) looking for O(nlogn) solution.)

Python Code

ll = [[6,9],[1,4],[3,5],[8,12]]

def SortSub(sub_li): 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 

ll = SortSub(ll)

def mergedList(a, b):
    return( [a[0], b[1]] )

nn = []
nn.append(ll[0])
for i in range(1,len(ll)):
    if(ll[i][0] < ll[i-1][1]):
        tt = nn.pop()
        nn.append( mergedList( tt , ll[i]) )
    else:
        nn.append(ll[i])

print(nn)