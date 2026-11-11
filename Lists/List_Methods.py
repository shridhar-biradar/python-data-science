# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.

lst = [1,2,3,5,2,22,56,7,8,43,21,56,12,21,34]
lst.sort() # (Original list is permanently changed)
print(f'asscending order of list: {lst}')

lst.sort(reverse=True) # (Original list is permanently changed)
print(f'descending order of list: {lst}') 

marks=[20,10,40,25,50]
sorted_marks= sorted(marks) # this creates a copy of original variable. original variable is unchanged
print(f"original marks: {marks}")
print(f"asscending order sorted marks: {sorted_marks}")

# sorting string by length of words
words = ['apple','cat','bulb','parrot']
sorted_words = sorted(words, key=len)
print(f"sorted words according to length of it: {sorted_words}")

num=[1,2,3,4]
print(f'original number list: {num}')
num.append(5)
num.append(10)
num.append(4)
print(f'Number list after appending some number: {num}')

num.insert(1,20)
print(f'Number list after inserting number at 1st position: {num}')

num.pop() # pop function it return the deleted value
print(f'Number list after pop function: {num}')

num.remove(4)
print(f'Number list after removing number 4: {num}')



