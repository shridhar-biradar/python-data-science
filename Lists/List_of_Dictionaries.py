# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.

"""
students_marks=[{
    'allen':89,
    },
    {
        'smith':78
    },
    {
        'david':99
    },
    {
        'alex':23
    }
    

]
print(students_marks)
for mark in students_marks:
    print(mark)
    for i in mark:
        print(mark[i])

"""


std={'a':1,'c':3,'b':2}
print(std)
std['c']=4
print(std)

std.update({'c':3,'d':4,'e':6})
print(std)

for i,j in std.items():
    print(f"{i} : {j}")

print(sorted(std.items(), reverse=True))


# sorting item by value using bubble sort
item=[]
for k in std:
    item.append((k,std[k]))

n=0
for _ in item:
    n+=1
print(item)
# start of bubble sorting
for i in range(n):
    for j in range(0,n-i-1):
        
        if item[j][1]>item[j+1][1]:
            item[j],item[j+1]=item[j+1],item[j]

sorted_by_values={}
for i,j in item:
    sorted_by_values[i]=std[i]

print(f'sorted by value : {sorted_by_values}')


# word count 
words=['a','a','b','c','d','d']
count={}
for i in words:
    count[i]=count.get(i,0)+1
print(count)

d1={'a':1,'b':2}
d2={'c':3,'d':4,'b':10}
merged_dict=d1 | d2
print('merged: ',merged_dict)