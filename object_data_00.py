# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s='Hello'
print(s[1],s[-4])

# Reverse the string
print(s[::-1])

# Build this list [0,0,0] two separate ways.
# method1:
print([0 for i in range(0,3) ])

# method2
my_list=[]
for x in range (0,3):
    my_list.append(0)
print(my_list)

# method3
print([0]*3)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

# Sort the list below:

list4 = [5,3,4,6,1]
list4.sort() #in place sorting affects the original array return none
sorted_list=sorted(list4) #return the sorted array
print(list4,sorted_list)

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
print(d['simple_key'],d.items())

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Can you sort a dictionary? Why or why not
# Answer: No! Because normal dictionaries are mappings not a sequence. 
# In Python, dictionaries themselves cannot be sorted in-place, but you can obtain a new dictionary with its items sorted by keys or values
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_by_key = dict(sorted(my_dict.items(),reverse=True))
print(sorted_by_key)